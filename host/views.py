from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Host
from category.models import Category
from .forms import HostForm


def all_hosts(request):
    """ A view to show all hosts, including sorting and search queries """

    hosts = Host.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                hosts = hosts.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            hosts = hosts.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            hosts = hosts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('hosts'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query))
            hosts = hosts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'hosts': hosts,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'host/hosts.html', context)


def host_detail(request, host_id):
    """ A view to show individual product details """

    host = get_object_or_404(Host, pk=host_id)

    # Gets product reviews from DB
    categories = host.category.filter.order_by('-rating', '-created_on')

    context = {
        'host': host,
        'categories': categories,
    }

    return render(request, 'host/host_detail.html', context)


@login_required
def add_host(request):
    """ Add host record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = HostForm(request.POST, request.FILES)
        if form.is_valid():
            host = form.save()
            messages.success(request, 'host Added Successfully')
            return redirect(reverse('host_detail', args=[host.id]))
        else:
            messages.error(request,
                           'Host Add Failed: Ensure The Form Is Valid.')
    else:
        form = HostForm()

    template = 'host/add_host.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_host(request, host_id):
    """ Edit a host record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    host = get_object_or_404(Host, pk=host_id)
    if request.method == 'POST':
        form = HostForm(request.POST, request.FILES, instance=host)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Host!')
            return redirect(reverse('host_detail', args=[host.id]))
        else:
            messages.error(request,
                           'Failed to update Host.'
                           ' Please ensure the form is valid.')
    else:
        form = HostForm(instance=host)
        messages.info(request, f'You are editing {host.hostname}')

    template = 'host/edit_host.html'
    context = {
        'form': form,
        'host': host,
    }

    return render(request, template, context)

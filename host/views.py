from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Host
from members.models import Members
from category.models import Category
from .forms import HostForm


def all_hosts(request):
    """ A view to show all hosts """

    hosts = Host.objects.all()
    familymembers = Members.objects.filter()
    categories = Category.objects.filter()

    context = {
        'hosts': hosts,
        'familymembers': familymembers,
        'categories': categories,
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
            return redirect(reverse('hosts'))
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

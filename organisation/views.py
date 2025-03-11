from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Organisation
from .forms import OrganisationForm


def all_organisations(request):
    """ A view to show all organisations """

    organisations = Organisation.objects.all()

    context = {
        'organisations': organisations,
    }

    return render(request, 'organisation/organisation.html', context)


def organisation_detail(request, organisation_id):
    """ A view to show individual organisation details """

    org = get_object_or_404(Organisation, pk=organisation_id)

    context = {
        'org': org,
    }

    return render(request, 'organisation/organisation_detail.html', context)


@login_required
def add_organisation(request):
    """ Add organisation record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = OrganisationForm(request.POST, request.FILES)
        if form.is_valid():
            organisation = form.save()
            messages.success(request, 'Organisation Added Successfully')
            return redirect(reverse('organisation_detail',
                                    args=[organisation.id]))
        else:
            messages.error(
                request, 'Organisation Add Failed: Ensure The Form Is Valid.')
    else:
        form = OrganisationForm()

    template = 'organisation/add_organisation.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_organisation(request, organisation_id):
    """ Edit a host record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    org = get_object_or_404(Organisation, pk=organisation_id)
    if request.method == 'POST':
        form = OrganisationForm(request.POST, request.FILES, instance=org)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Organisation!')
            return redirect(reverse('organisation_detail', args=[org.id]))
        else:
            messages.error(request,
                           'Failed to update Organisation.'
                           ' Please ensure the form is valid.')
    else:
        form = OrganisationForm(instance=org)
        messages.info(request, f'You are editing {Organisation.orgname}')

    template = 'organisation/edit_orgaanisation.html'
    context = {
        'form': form,
        'org': org,
    }

    return render(request, template, context)

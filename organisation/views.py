from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Organisation
from teamlead.models import Teamlead
from .forms import OrganisationForm


def all_organisations(request):
    """ A view to show all organisations """

    organisations = Organisation.objects.all()
    teamleaders = Teamlead.objects.all()

    # get all teamleaders and filter in html.
    # number of organisations is small and number of teamleaders
    # is mall so no real processing overhead

    context = {
        'organisations': organisations,
        'teamleaders': teamleaders,
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
            form.save()
            messages.success(request, 'Organisation Added Successfully')
            return redirect(reverse('organisation'))
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

    organisation = get_object_or_404(Organisation, pk=organisation_id)
    if request.method == 'POST':
        form = OrganisationForm(request.POST, request.FILES,
                                instance=organisation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Organisation!')
            return redirect(reverse('organisation'))
        else:
            messages.error(request,
                           'Failed to update Organisation.'
                           ' Please ensure the form is valid.')
    else:
        form = OrganisationForm(instance=organisation)
        messages.info(request, f'You are editing: {organisation.orgname}')

    template = 'organisation/edit_organisation.html'
    context = {
        'form': form,
        'organisation': organisation,
    }

    return render(request, template, context)


@login_required
def delete_organisation(request, organisation_id):
    """ Delete an organisation record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    organisation = get_object_or_404(Organisation, pk=organisation_id)
    organisation.delete()
    messages.success(request,
                     f'Organisation: {organisation.orgname}'
                     f' Successfully deleted')
    return redirect(reverse('organisation'))

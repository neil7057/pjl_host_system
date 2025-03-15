from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Teamlead
from .forms import TeamleadForm


def all_teamleads(request):
    """ A view to show all teamleader """

    teamleaders = Teamlead.objects.all()

    context = {
        'teamleaders': teamleaders,
    }

    return render(request, 'teamlead/teamlead.html', context)


@login_required
def add_teamlead(request):
    """ Add teamleader record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TeamleadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team Leader Added Successfully')
            return redirect(reverse('teamlead'))
        else:
            messages.error(
                request, 'Team Leader Add Failed: Ensure The Form Is Valid.')
    else:
        form = TeamleadForm()

    template = 'teamlead/add_teamlead.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_teamlead(request, teamlead_id):
    """ Edit a team leader record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    teamlead = get_object_or_404(Teamlead, pk=teamlead_id)
    if request.method == 'POST':
        form = TeamleadForm(request.POST, request.FILES, instance=teamlead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Team Leader!')
            return redirect(reverse('teamlead'))
        else:
            messages.error(request,
                           'Failed to update Team Leader.'
                           ' Please ensure the form is valid.')
    else:
        form = TeamleadForm(instance=teamlead)
        messages.info(request,
                      f'You are editing {teamlead.first_name}'
                      f' {teamlead.last_name}')

    template = 'teamlead/edit_teamlead.html'
    context = {
        'form': form,
        'teamlead': teamlead,
    }

    return render(request, template, context)


@login_required
def delete_teamlead(request, teamlead_id):
    """ Delete a Team Leader record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    teamlead = get_object_or_404(Teamlead, pk=teamlead_id)
    teamlead.delete()
    messages.success(request,
                     f'Team Leader: {teamlead.first_name} {teamlead.last_name}'
                     f' Successfully deleted')
    return redirect(reverse('teamlead'))

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

    return render(request, 'teamlead/teamleaders.html', context)


def teamlead_detail(request, teamlead_id):
    """ A view to show individual team leader details """

    teamleader = get_object_or_404(Teamlead, pk=teamlead_id)

    context = {
        'teamleader': teamleader,
    }

    return render(request, 'teamlead/teamleader_detail.html', context)


@login_required
def add_teamlead(request):
    """ Add teamleader record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TeamleadForm(request.POST, request.FILES)
        if form.is_valid():
            teamlead = form.save()
            messages.success(request, 'Team Leader Added Successfully')
            return redirect(reverse('teamleader_detail',
                                    args=[teamlead.id]))
        else:
            messages.error(
                request, 'Team Leader Add Failed: Ensure The Form Is Valid.')
    else:
        form = TeamleadForm()

    template = 'teamlead/add_teamleader.html'
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

    teamleader = get_object_or_404(Teamlead, pk=teamlead_id)
    if request.method == 'POST':
        form = TeamleadForm(request.POST, request.FILES, instance=teamleader)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Team Leader!')
            return redirect(reverse('teamleader_detail', args=[teamleader.id]))
        else:
            messages.error(request,
                           'Failed to update Team Leader.'
                           ' Please ensure the form is valid.')
    else:
        form = TeamleadForm(instance=teamleader)
        messages.info(request, f'You are editing {Teamlead.first_name}')

    template = 'teamlead/edit_teamleader.html'
    context = {
        'form': form,
        'teamleader': teamleader,
    }

    return render(request, template, context)

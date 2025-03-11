from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Timeperiod
from .forms import TimeperiodForm


def all_timeperiods(request):
    """ A view to show all time periods"""

    timeperiods = Timeperiod.objects.all()

    context = {
        'timeperiods': timeperiods,
    }

    return render(request, 'timeperiod/timeperiod.html', context)


def timeperiod_detail(request, timeperiod_id):
    """ A view to show individual team time period details """

    timeperiod = get_object_or_404(Timeperiod, pk=timeperiod_id)

    context = {
        'timeperiod': timeperiod,
    }

    return render(request, 'timeperiod/timeperiod_detail.html', context)


@login_required
def add_timeperiod(request):
    """ Add timeperiod record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TimeperiodForm(request.POST, request.FILES)
        if form.is_valid():
            timeperiod = form.save()
            messages.success(request, 'timeperiod Added Successfully')
            return redirect(reverse('timeperiod'))
        else:
            messages.error(
                request, 'timeperiod Add Failed: Ensure The Form Is Valid.')
    else:
        form = TimeperiodForm()

    template = 'timeperiod/add_timeperiod.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_timeperiod(request, timeperiod_id):
    """ Edit a timeperiod record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    timeperiod = get_object_or_404(Timeperiod, pk=timeperiod_id)
    if request.method == 'POST':
        form = TimeperiodForm(request.POST, request.FILES, instance=timeperiod)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Time period!')
            return redirect(reverse('timeperiod_detail', args=[timeperiod.id]))
        else:
            messages.error(request,
                           'Failed to update timeperiod.'
                           ' Please ensure the form is valid.')
    else:
        form = TimeperiodForm(instance=timeperiod)
        messages.info(request, f'You are editing {Timeperiod.first_name}')

    template = 'timeperiod/edit_timeperiod.html'
    context = {
        'form': form,
        'timeperiod': timeperiod,
    }

    return render(request, template, context)

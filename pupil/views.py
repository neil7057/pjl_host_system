from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Pupil
from .forms import PupilForm


def all_pupils(request):
    """ A view to show all organisations """

    pupils = Pupil.objects.all()

    context = {
        'pupils': pupils,
    }

    return render(request, 'pupil/pupils.html', context)


def pupil_detail(request, pupil_id):
    """ A view to show individual pupils details """

    pupil = get_object_or_404(Pupil, pk=pupil_id)

    context = {
        'pupil': pupil,
    }

    return render(request, 'pupil/pupil_detail.html', context)


@login_required
def add_pupil(request):
    """ Add pupil record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PupilForm(request.POST, request.FILES)
        if form.is_valid():
            pupil = form.save()
            messages.success(request, 'Pupil Added Successfully')
            return redirect(reverse('pupils'))
        else:
            messages.error(request,
                           'Pupil Add Failed: Ensure The Form Is Valid.')
    else:
        form = PupilForm()

    template = 'pupil/add_pupil.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_pupil(request, pupil_id):
    """ Edit a pupil record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    pupil = get_object_or_404(Pupil, pk=pupil_id)
    if request.method == 'POST':
        form = PupilForm(request.POST, request.FILES, instance=pupil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Pupil!')
            return redirect(reverse('pupil_detail', args=[pupil.id]))
        else:
            messages.error(request,
                           'Failed to update Pupil.'
                           ' Please ensure the form is valid.')
    else:
        form = PupilForm(instance=pupil)
        messages.info(request, f'You are editing {Pupil.first_name}')

    template = 'pupil/edit_pupil.html'
    context = {
        'form': form,
        'pupil': pupil,
    }

    return render(request, template, context)

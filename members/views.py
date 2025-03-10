from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Members
from .forms import MembersForm


def all_members(request, Host_id):
    """ A view to show all members, including sorting and search queries """

    member = Members.objects.all().filter(Members.host_id == Host_id)

    context = {
        'members': member,
    }

    return render(request, 'members/members.html', context)


def members_detail(request, Members_id):
    """ A view to show individual Members details """

    Member = get_object_or_404(Members, pk=Members_id)

    context = {
        'Members': Member,
    }

    return render(request, 'members/Members_detail.html', context)


@login_required
def add_members(request):
    """ Add Members to shop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES)
        if form.is_valid():
            Members = form.save()
            messages.success(request, 'Member Record Added Successfully')
            return redirect(reverse('Members_detail', args=[Members.id]))
        else:
            messages.error(request,
                           'Member record Add Failed: Ensure Form Is Valid')
    else:
        form = MembersForm()

    template = 'members/add_Members.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_members(request, Members_id):
    """ Edit a Member record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    Member = get_object_or_404(Members, pk=Members_id)
    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES, instance=Member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Member record!')
            return redirect(reverse('Members_detail', args=[Members.id]))
        else:
            messages.error(request,
                           'Failed to update Member record.'
                           ' Please ensure the form is valid.')
    else:
        form = MembersForm(instance=Members)
        messages.info(request, f'You are editing {Members.name}')

    template = 'members/edit_Members.html'
    context = {
        'form': form,
        'Members': Members,
    }

    return render(request, template, context)


@login_required
def delete_members(request, Members_id):
    """ Delete a Member record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    Member = get_object_or_404(Members, pk=Members_id)
    Member.delete()
    messages.success(request, 'Member Successfully deleted')
    return redirect(reverse('members'))

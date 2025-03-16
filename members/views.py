from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Members
from .forms import MembersForm


def all_members(request):
    """ A view to show all members,  """

    members = Members.objects.all()

    context = {
        'members': members,
    }

    return render(request, 'members/members.html', context)


def member_detail(request, Members_id):
    """ A view to show individual Members details """

    Member = get_object_or_404(Members, pk=Members_id)

    context = {
        'Members': Member,
    }

    return render(request, 'members/Members_detail.html', context)


@login_required
def add_member(request):
    """ Add Members to shop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member Record Added Successfully')
            return redirect(reverse('members'))
        else:
            messages.error(request,
                           'Member record Add Failed: Ensure Form Is Valid')
    else:
        form = MembersForm()

    template = 'members/add_Member.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_member(request, members_id):
    """ Edit a Member record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    member = get_object_or_404(Members, pk=members_id)
    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Member record!')
            return redirect(reverse('members'))
        else:
            messages.error(request,
                           'Failed to update Member record.'
                           ' Please ensure the form is valid.')
    else:
        form = MembersForm(instance=member)
        messages.info(request, f'You are editing'
                               f' {member.first_name} '
                               f'{member.last_name}')

    template = 'members/edit_member.html'
    context = {
        'form': form,
        'member': member,
    }

    return render(request, template, context)


@login_required
def delete_member(request, members_id):
    """ Delete a Member record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    Member = get_object_or_404(Members, pk=members_id)
    Member.delete()
    messages.success(request, 'Member Successfully deleted')
    return redirect(reverse('members'))

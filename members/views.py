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


def all_members_for_host(request, Host_id):
    """ A view to show all members, including sorting and search queries """

    members = Members.objects.all().filter(Members.host_id == Host_id)

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
            Members = form.save()
            messages.success(request, 'Member Record Added Successfully')
            return redirect(reverse('Member_detail', args=[Members.id]))
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
def edit_member(request, Members_id):
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
            return redirect(reverse('Member_detail', args=[Members.id]))
        else:
            messages.error(request,
                           'Failed to update Member record.'
                           ' Please ensure the form is valid.')
    else:
        form = MembersForm(instance=Members)
        messages.info(request, f'You are editing {Members.name}')

    template = 'members/edit_Member.html'
    context = {
        'form': form,
        'Members': Members,
    }

    return render(request, template, context)


@login_required
def delete_member(request, Members_id):
    """ Delete a Member record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    Member = get_object_or_404(Members, pk=Members_id)
    Member.delete()
    messages.success(request, 'Member Successfully deleted')
    return redirect(reverse('members'))

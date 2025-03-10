from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Category
from .forms import CategoryForm


def all_category(request, Host_id):
    """ A view to show all categories """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'category/categories.html', context)


@login_required
def add_category(request):
    """ Add Category """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Category Record Added Successfully')
            return redirect(reverse('all_categories'))
        else:
            messages.error(request,
                           'Category record Add Failed: Ensure Form Is Valid')
    else:
        form = CategoryForm()

    template = 'category/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_category(request, Category_id):
    """ Edit a Category record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=Category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Catgeory record!')
            return redirect(reverse('all_categories'))
        else:
            messages.error(request,
                           'Failed to update Category record.'
                           ' Please ensure the form is valid.')
    else:
        form = CategoryForm(instance=Category)
        messages.info(request, f'You are editing {Category.name}')

    template = 'category/edit_category.html'
    context = {
        'form': form,
        'Categories': Category,
    }

    return render(request, template, context)


@login_required
def delete_category(request, Category_id):
    """ Delete a category record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=Category_id)
    category.delete()
    messages.success(request, 'Category Successfully deleted')
    return redirect(reverse('category'))

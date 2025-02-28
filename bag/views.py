from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view to display bag contents """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, (
                        f'You updated size {size.upper()}'
                        f' {product.name} quantity to'
                        f' {bag[item_id]["items_by_size"][size]}'))
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, (
                        f'You added size {size.upper()}'
                        f' {product.name} to your Shopping Bag'))
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, (
                    f'You added size {size.upper()}'
                    f' {product.name} to your Shopping Bag'))
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, (
                    f'You updated {product.name}'
                    f' quantity to {bag[item_id]}'))
        else:
            bag[item_id] = quantity
            messages.success(
                request, (
                    f'You added {product.name}'
                    f' to your Shopping Bag'))

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the qty of a specified product already in the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if quantity < 1 or quantity > 9:
        messages.error(
            request, 'Quantity must be in the range 1 to 9')
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, (
                    f'You have updated size {size.upper()} {product.name}'
                    f' quantity to {bag[item_id]["items_by_size"][size]}'))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, (
                    f'You have removed size {size.upper()}'
                    f' {product.name} from your Shopping Bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, (
                    f'You have updated {product.name}'
                    f' quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(
                request, (
                    f'You have removed {product.name}'
                    f' from your Shopping Bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ A view to Remove an item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, (
                    f'You have updated size {size.upper()}'
                    f' {product.name} quantity to'
                    f' {bag[item_id]["items_by_size"][size]}'))
        else:
            bag.pop(item_id)
            messages.success(
                request, (
                    f'You have removed {product.name}'
                    f' from your Shopping Bag'))

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

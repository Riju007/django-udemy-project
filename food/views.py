"""View for the app food."""
from django.shortcuts import redirect, render

from food.models import Item
from food.forms import ItemForm


def home(request):
    """Home page for the food app."""
    return render(request, 'food/home.html')


def list_item(request):
    """List of all the food items."""
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    # render method signature - render(request, template_name, context)
    return render(request, 'food/item_list.html', context)


def view_item(request, item_id):
    """Detail of a food item."""
    item = Item.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'food/detail.html', context)


def create_item(request):
    """Create a food item."""
    form = ItemForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        print(form.cleaned_data.get('item_price'))
        form.save()
        return redirect('food:index_view')
    return render(request, 'food/item_form.html', {'form': form})


def update_item(request, id):
    """Update a food item."""
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index_view')
    return render(request, 'food/item_form.html', {'form': form, 'item': item})


def delete_item(request, id):
    """Delete a food item."""
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index_view')

    return render(request, 'food/item_delete.html', {'item': item})

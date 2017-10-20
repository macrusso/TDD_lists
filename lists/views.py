from django.shortcuts import redirect, render, get_object_or_404
from lists.forms import ExistingListItemForm, ItemForm, DeleteItemForm, DeleteListForm
from lists.models import List, Item


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


def view_list(request, list_id):
    list_ = get_object_or_404(List, pk=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

def delete_list(request, list_id):
    list = get_object_or_404(List, pk=list_id)

    if request.method == 'POST':
        form = DeleteListForm(request.POST, instance=list)

        if form.is_valid():
            list.delete()
            return redirect('home')

def delete_item(request, list_id, item_id):
    todo_list = get_object_or_404(List, pk=list_id)
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = DeleteItemForm(request.POST, instance=item)

        if form.is_valid():
            item.delete()
            return redirect(todo_list)

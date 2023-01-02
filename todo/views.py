from django.shortcuts import get_object_or_404, redirect, render
from todo.forms import TodoForm, TypeForm
from todo.models import Todo, Type



# Create your views here.


# def todo_list(request):
#     todos = Todo.objects.order_by('todo')
#     return render(request, 'todo/todo_list.html', {'todos': todos})

# SELECT JOIN: select_related()
def todo_list(request):
    todos = Todo.objects.select_related('type').order_by('todo')
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/todo_detail.html',{'todo': todo})


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid:
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form})


def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid:
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo/todo_edit.html', {'form': form})


# ---------------------------------------- TYPE -------------------------------------------------
def type_list(request):
    types = Type.objects.order_by('type')
    return render(request, 'todo/type_list.html', {'types': types})


def type_new(request):
    if request.method == "POST":
        form = TypeForm(request.POST)
        if form.is_valid:
            type = form.save(commit=False)
            type.save()
            return redirect('type_detail', pk=type.pk)
    else:
        form = TypeForm()
    return render(request, 'todo/type_edit.html', {'form': form})


def type_detail(request, pk):
    type = get_object_or_404(Type, pk=pk)
    return render(request, 'todo/type_detail.html', {'type': type})


def type_edit(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == "POST":
        form = TypeForm(request.POST, instance=type)
        if form.is_valid:
            type = form.save(commit=False)
            type.save()
            return redirect('type_detail', pk=type.pk)
    else:
        form = TypeForm(instance=type)
    return render(request, 'todo/type_edit.html', {'form': form})

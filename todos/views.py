from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.forms.models import modelform_factory
from todos.models import Todo
from todos.forms import TodoForm

def index(request):
    form = modelform_factory(Todo, fields=('title',))
    latest_todo_list = Todo.objects.all().order_by('closed', '-pub_date')
    return render(request, 'todos/index.html',
            {'latest_todo_list': latest_todo_list, 'form': form})

def add(request):
    title = request.POST['title']
    if title == '':
        messages.info(request, 'todo title required')
    else:
        todo = Todo(title=title)
        todo.save()
    return HttpResponseRedirect(reverse('todos:index'))

def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    form = TodoForm(instance=todo)
    return render(request, 'todos/edit.html',
            {'todo': todo, 'form': form })

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    form = TodoForm(request.POST, instance=todo)
    form.save()
    return HttpResponseRedirect(reverse('todos:index'))

def close(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.closed = True
    todo.save()
    return HttpResponseRedirect(reverse('todos:index'))

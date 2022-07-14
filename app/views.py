from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskEdit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.messages.views import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def register(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            messages.info(request, 'Details incorrect')
            return redirect('register')

    context = {'form': form}
    return render(request, 'login-register.html', context)


def customlogin(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login details')

    context = {'page': page}
    return render(request, 'login-register.html', context)


def customlogout(request):

    logout(request)
    return redirect('login')


@login_required(login_url='login')
def taskcreate(request):

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        task = Task.objects.create(user=request.user, title=title, description=description)

        task.save()
        return redirect('/')

    context = {}
    return render(request, 'task-create.html', context)


@login_required(login_url='login')
def taskdelete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'task-delete.html', context)


@login_required(login_url='login')
def taskedit(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskEdit(instance=task)

    if request.method == 'POST':
        form = TaskEdit(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'task': task, 'form': form}
    return render(request, 'task-edit.html', context)


@login_required(login_url='login')
def taskdetail(request, pk):
    task = Task.objects.get(id=pk)

    context = {'task': task}
    return render(request, 'task-detail.html', context)


@login_required(login_url='login')
def tasklist(request):
    tasks = Task.objects.filter(user=request.user)
    count = tasks.filter(completed=False).count()
    search_input = request.GET.get('search_area') or ''

    if search_input:
        tasks = Task.objects.filter(user=request.user, title__icontains=search_input)
    else:
        tasks = Task.objects.filter(user=request.user)

    context = {'tasks': tasks, 'count': count, 'search_input': search_input}
    return render(request, 'task-list.html', context)


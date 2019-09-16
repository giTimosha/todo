from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article
from django.http import HttpResponseRedirect
from django.urls import reverse
from webapp.forms import ArticleForm


def index_views(request, *args, **kwargs):
    tasks = Article.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_view(request, pk):
    task = get_object_or_404(Article, pk=pk)
    print(pk)
    return render(request, 'task_view.html', context={'task':task})


def total_view(request, pk):
    task = get_object_or_404(Article, pk=pk)
    context = {'task': task}
    return render((request, 'total.html', context))


def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'task_create.html', context={'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                description=form.cleaned_data['description'],
                total_description=form.cleaned_data['total_description'],
                status=form.cleaned_data['status'],
                date=form.cleaned_data['date']
            )
            return redirect('task_view', pk=article.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})


def task_update_view(request, pk):
    task = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(data={
            'description': task.description,
            'total_description': task.total_description,
            'status': task.status,
            'date': task.date
        })
        return render(request, 'update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.total_description = form.cleaned_data['total_description']
            task.status = form.cleaned_data['status']
            task.date = form.cleaned_data['date']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'article': task})


def task_delete(request, pk):
    todo = Article.objects.get(pk=pk)
    todo.delete()
    tasks = Article.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})

# coding: utf-8
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blogs.models import Entry, Tag


def entry_list(request, username=None, tag=None):
    if username:
        entries = Entry.objects.filter(user__username=username)
    else:
        entries = Entry.objects.all()

    if tag:
        entries = entries.filter(tags__name=tag)

    paginator = Paginator(entries, 3)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    return render(request, 'blogs/entry_list.html', {'entries': entries})


def user_list(request):
    users = User.objects.all().order_by('username')
    return render(request, 'blogs/user_list.html', {'users': users})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blogs/tag_list.html', {'tags': tags})


@login_required(login_url='/blogs/login')
def create_entry(request):
    if request.method == 'GET':
        return render(request, 'blogs/create_entry.html')
    elif request.method == 'POST':
        if request.POST['title'] == '' or request.POST['contents'] == '':
            messages.error(request, u'Field(s) empty error')
            return HttpResponseRedirect(reverse('blogs:create_entry'))
        entry = Entry()
        entry.user = request.user
        entry.title = request.POST['title']
        entry.contents = request.POST['contents']
        entry.pub_date = timezone.now()
        entry.save()
        if request.POST['tags'] != '':
            tags = request.POST['tags'].split()
            for tag in tags:
                entry.tags.add(Tag.objects.get_or_create(name=tag)[0])
            entry.save()
        return HttpResponseRedirect(reverse('blogs:index'))


def detail_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blogs/entry_list.html', {'entries': [entry]})


@login_required(login_url='/blogs/login')
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blogs/edit_entry.html', {'entry': entry})


@login_required(login_url='/blogs/login')
def update_entry(request, entry_id):
    if request.POST['title'] == '' or request.POST['contents'] == '':
        messages.error(request, u'Field(s) empty error')
        return HttpResponseRedirect(reverse('blogs:edit_entry', args=[entry_id]))
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.title = request.POST['title']
    entry.contents = request.POST['contents']
    entry.tags.clear()
    if request.POST['tags'] != '':
        tags = [tag.strip() for tag in request.POST['tags'].split(',')]
        for tag in tags:
            entry.tags.add(Tag.objects.get_or_create(name=tag)[0])
    entry.save()
    return HttpResponseRedirect(reverse('blogs:detail_entry', args=[entry_id]))


@login_required(login_url='/blogs/login')
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    entry.delete()
    return HttpResponseRedirect(reverse('blogs:index'))


def user_login(request):
    if request.method == 'GET':
        next_path = request.GET.get('next', reverse('blogs:index'))
        return render(request, 'blogs/login.html', {'next': next_path})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, u'ログインしました')
                return HttpResponseRedirect(request.POST['next'])
            else:
                messages.error(request, u'無効なユーザーです')
                return HttpResponseRedirect(reverse('blogs:login'))
        else:
            messages.error(request, u'ログインに失敗しました')
            return HttpResponseRedirect(reverse('blogs:login'))


def user_logout(request):
    logout(request)
    messages.success(request, u'ログアウトしました')
    return HttpResponseRedirect(reverse('blogs:index'))

# django imports
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F

# app imports
from stats.models import Developer
from stats.forms import DeveloperCreateForm


def developer_list(request):
    developers = Developer.objects.all()
    return render(request,
                  'developer/list.html',
                  {'developers': developers})


def developer_detail(request, username):
    developer = get_object_or_404(Developer, username=username)
    # top repositories by number of stars + watchers + forks
    fields_op = F('stargazers_count') + F('watchers_count') + F('forks_count')
    top_repos = developer.repos.annotate(counts_sum=fields_op)\
                               .order_by('-counts_sum')[:5]
    return render(request,
                  'developer/detail.html',
                  {'developer': developer,
                   'top_repos': top_repos})


def developer_create(request):
    if request.method == 'POST':
        # form was submitted
        form = DeveloperCreateForm(request.POST)
        if form.is_valid():
            # access form cleaned data
            username = form.cleaned_data['username']
            developer = Developer.objects.create(username=username)
            developer.update_profile_from_github()
            developer.update_repos_from_github()

            # redirect to developer detail
            return redirect('developer_detail', username=username)
    else:
        form = DeveloperCreateForm()
    return render(request,
                  'developer/create.html',
                  {'form': form})

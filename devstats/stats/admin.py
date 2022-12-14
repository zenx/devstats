# django imports
from django.contrib import admin

# project imports
from stats.models import Developer, Repo


@admin.register(Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = ['name', 'developer', 'stargazers_count', 'watchers_count',
                    'forks_count']
    search_fields = ['name']


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'location', 'company', 'website_url',
                    'total_followers', 'total_following']
    search_fields = ['username', 'name', 'company', 'website_url']

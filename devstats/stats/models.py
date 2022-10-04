# 3rd. party imports
from github import Github, GithubException

# django imports
from django.conf import settings
from django.db import models


class Developer(models.Model):
    username = models.CharField(max_length=100,
                                unique=True)
    name = models.CharField(max_length=100,
                            blank=True)
    location = models.CharField(max_length=100,
                                blank=True)
    company = models.CharField(max_length=100,
                               blank=True)
    avatar_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    # counts
    total_followers = models.PositiveIntegerField(default=0)
    total_following = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gh_user = None

    def __str__(self):
        return self.username

    def _get_github_user(self):
        """
        Retrieves a GitHub User
        """
        if not self._gh_user:
            # github API auth
            gh = Github(settings.GITHUB_TOKEN,
                        per_page=settings.GITHUB_OBJECTS_PER_PAGE)
            # retrieve github user profile
            self._gh_user = gh.get_user(self.username)
        return self._gh_user

    def update_profile_from_github(self):
        """
        Updates developer profile data from the GitHub API
        """
        gh_user = self._get_github_user()
        # update fields
        self.name = gh_user.name or ''
        self.location = gh_user.location or ''
        self.avatar_url = gh_user.avatar_url or ''
        self.website_url = gh_user.blog or ''
        self.company = gh_user.company or ''
        self.total_followers = gh_user.followers
        self.total_following = gh_user.following

        # save model
        self.save()

    def update_repos_from_github(self):
        """
        Creates/updates user repositories from the Github API
        """
        # retrieve github user repos
        gh_repos = self._get_github_user().get_repos(type='owner')
        for gh_repo in gh_repos:
            # create repository if necessary
            repo, created = self.repos.get_or_create(name=gh_repo.name)
            # update repository stats
            repo.stargazers_count = gh_repo.stargazers_count
            repo.watchers_count = gh_repo.watchers_count
            repo.forks_count = gh_repo.forks_count
            # save repository to DB
            repo.save()


class Repo(models.Model):
    developer = models.ForeignKey(Developer,
                                  related_name='repos',
                                  on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    stargazers_count = models.PositiveIntegerField(default=0)
    watchers_count = models.PositiveIntegerField(default=0)
    forks_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = [('developer', 'name')]

    def __str__(self):
        return f'{self.developer.username}/{self.name}'

    def get_github_url(self):
        return 'https://github.com/' + self.__str__()

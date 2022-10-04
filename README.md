# devstats
Sample Django project using the Github API

## Instructions

1. Generate a Github personal access token at https://github.com/settings/tokens inclduing the `repo` and `user` scopes.
2. Add the token to the `GITHUB_TOKEN` environment variable or to the `GITHUB_TOKEN` setting in `settings.py`
3. Install requirements with `pip install requirements.txt`
4. Execute database migrations with `python manage.py migrate`
5. Run the project on your local machine with the command `python manage.py runserver`
6. To access the admin back-end create a superuser with `python manage.py createsuperuser`

## Additional Resources
- PyGithub docs – https://pygithub.readthedocs.io/
- Github API docs – https://docs.github.com/en/rest

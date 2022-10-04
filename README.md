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
- Django models – https://docs.djangoproject.com/en/4.1/topics/db/models/
- Many-to-one relationships – https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
- Django forms – https://docs.djangoproject.com/en/4.1/topics/forms/
- Django form field validation – https://docs.djangoproject.com/en/4.1/ref/forms/validation/
- Making queries with the Django ORM – https://docs.djangoproject.com/en/4.1/topics/db/queries/
- Using `annotate()` to generate aggregates for each item in a QuerySet – https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset
- Django `F()` query expressions – https://docs.djangoproject.com/en/4.1/ref/models/expressions/
- Serving static files during development – https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-static-files-during-development
- PyGithub docs – https://pygithub.readthedocs.io/
- Github API docs – https://docs.github.com/en/rest

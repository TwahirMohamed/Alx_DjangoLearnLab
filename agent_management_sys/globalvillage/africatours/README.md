# File structure and function of each file in the app
```text
Django project - It is the entire web application.
Configuration and collection of apps that together make up a website.
Composition of a project"
1. settings.py → global settings (databases, installed apps, middleware…)

2. urls.py → the main URL routing

3. wsgi.py/asgi.py → entry points for the web server

4. manage.py script → runserver, migrations, etc.

Django App - An app is a specific piece of functionality inside a project.

Examples: a blog system, a user authentication system, a payments module.

Each app is meant to be reusable and self-contained.

An app usually has:

1. models.py → database tables

2. views.py → logic for requests/responses

3. urls.py → routing for just that app

4. templates/ → HTML for that feature

5. static/ → CSS, JS, images for that feature

Think of an app as one feature of your site.
# Django Vue Demo

This is a simple list-keeping app that will serve to demonstrate the use of Django in conjunction with the Vue frontend framework.

## Technologies Used

- Django
- Django REST Framework
- Vue
- Webpack

## Requirements

- SQLite 3
- Python 3.6.5
- pip
    - django
    - djangorestframework

## Setup

1. Clone the project.

   `git clone https://github.com/cpgillem/django-vue-demo.git`

1. Copy the settings.py.example file and fill in the SECRET_KEY setting.

   `cd django-vue-demo && cp django_vue_demo/settings.py.example django_vue_demo/settings.py`

1. Run the migrations.

   `python manage.py migrate`

1. Run the server.

   `python manage.py runserver`

## API Reference

### List
`url: /api/lists/`

A list represents a collection of items. It has a title and a one-to-many relationship to the items.

### Item
`url: /api/items/`

An item has a title and a boolean representing whether it is archived, checked, done, etc.

### Profile
`url: /api/profiles/`

Profiles represent users who own multiple lists.

# Further Reading

- https://ariera.github.io/2017/09/26/django-webpack-vue-js-setting-up-a-new-project-that-s-easy-to-develop-and-deploy-part-1.html
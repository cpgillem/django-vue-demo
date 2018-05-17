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
- npm

## Setup

1. Clone the project.

   `git clone https://github.com/cpgillem/django-vue-demo.git`

1. Change directories.

   `cd django-vue-demo`

1. Copy the settings.py.example file and fill in the SECRET_KEY setting.

   `cp django_vue_demo/settings.py.example django_vue_demo/settings.py`

1. Install the npm dependencies.

   `npm install`

1. Run webpack.

   `npx webpack`

1. Run the migrations.

   `python manage.py migrate`

1. Run the server.

   `python manage.py runserver`

## Compiling Assets

To compile the frontend's assets, run `npx webpack`. This should place a bundle in the assets/bundles directory. After running `python manage.py collectstatic`, this file should be available to the Django.

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
- https://github.com/michaelbukachi/django-vuejs-tutorial/wiki/Django-Vue.js-Integration-Tutorial
- https://owais.lone.pw/blog/webpack-plus-reactjs-and-django/
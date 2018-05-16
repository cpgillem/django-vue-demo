# Django Vue Demo

This is a simple list-keeping app that will serve to demonstrate the use of Django in conjunction with the Vue frontend framework.

## Technologies Used

- Django
- Django REST Framework
- Vue
- Webpack

## API Reference

### List
`url: /lists/`

A list represents a collection of items. It has a title and a one-to-many relationship to the items.

### Item
`url: /items/`

An item has a title and a boolean representing whether it is archived, checked, done, etc.

### User
`url: /users/`

Users are used to authenticate to the API. They also own multiple lists.
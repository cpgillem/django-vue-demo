# Django Vue Demo

This is a simple list-keeping app that will serve to demonstrate the use of Django in conjunction with the Vue frontend framework.

## Technologies Used

- Django
- Django REST Framework
- Vue
- Webpack

## API Reference

### List
`url: /api/lists/`

A list represents a collection of items. It has a title and a one-to-many relationship to the items.

### Item
`url: /api/items/`

An item has a title and a boolean representing whether it is archived, checked, done, etc.

### User
`url: /api/users/`

Users are used to authenticate to the API. They also own multiple lists.
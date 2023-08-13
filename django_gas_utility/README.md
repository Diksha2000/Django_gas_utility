# Django_Gas_Utility
This is a gas utility app that allow customers to submit service requests online, track the status of their requests, and view their account information. 

Below is the basic Structure of the django gas utility application codebase

gas_utility_app/       # Application root directory

|-- consumer/           # Main application module

|   |-- migrations/     # Database migration files

|   |-- templates/      # HTML template files

        |--account_info.html
        
        |--base.html
        
        |--home.html
        
        |--submit_request.html
        
        |--track_request.html
        
|   |-- __init__.py     # Python package initializer

|   |-- admin.py        # Admin panel configuration

|   |-- apps.py         # Application configuration

|   |-- forms.py        # Form classes for data validation

|   |-- models.py       # Database models

|   |-- urls.py         # URL routing for the application

|   |-- views.py        # View functions and classes

|-- django_gas_utility/ # Project settings and configuration

|   |-- __init__.py

|   |-- settings.py     # Project settings file

|   |-- urls.py         # Project-level URL routing

|   |-- wsgi.py         # WSGI configuration for deployment

|   |-- asgi.py         # ASGI configuration for asynchronous server

|-- support/            # Support application module

|   |-- migrations/     # Database migration files

|   |-- templates/      # HTML template files

|   |-- __init__.py     # Python package initializer

|   |-- admin.py        # Admin panel configuration

|   |-- apps.py         # Application configuration

|   |-- models.py       # Database models for support tasks

|   |-- urls.py         # URL routing for the support application

|   |-- views.py        # View functions and classes for support
|-- manage.py           # Django management script



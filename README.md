# recipe-app

- This application uses the Django web framework to develop a fully-fledged web application with multiple users and an admin panel. 
- This app lets users sign up and create their own content it has statistical dashboards to show data analytics and data visualization..
-  It is made with coding's best practices like being well-tested and well-documented code on GitHub.

## Table of Contents
- [Features](#Features)
- [Screenshots](#Screenshots)
- [Technical_Requirements](#Technical_Requirements)
- [Dependencies](#Dependencies)
- [Environment](#Environment)

## Features
- Allows for user authentication, login, and logout.
- Lets users search for recipes according to difficulty.
- Receives user input and handle errors appropriately.
- Displays more details on each recipe if the user asks for them.
- Adds user recipes to an SQLite database.
- Includes a Django Admin dashboard for working with database entries.
- Shows statistics and visualizations based on trends and data analysis.

## Screenshots

<img src ="https://github.com/hakobya4/recipe-app/assets/108638724/cf9051e8-440c-4ceb-9a96-bd15fccb0025" width="400" height="250"/>
<img src ="https://github.com/hakobya4/recipe-app/assets/108638724/d8e37aa9-0f61-4822-a195-17d0b452063c" width="400" height="250"/>
<img src ="https://github.com/hakobya4/recipe-app/assets/108638724/dc06cd59-6e6c-45c3-8c9d-b3509a6f4d74" width="400" height="250"/>

## Technical_Requirements
- Works on Python 3.6+ installations and Django version 3.
- Handles exceptions or errors that arise during user input.
- Connects to a PostgreSQL database hosted locally on the same system.
- Provides an easy-to-use interface, supported by simple forms of input and concise, easy-to-follow instructions.
- A “requirements.txt” file is provided, containing the requisite modules for the project.

## Dependencies
To install the dependencies for this app run pip install -r requirements.txt
- Django
- Gunicorn
- White Noise
- Psycopg2-binary
- Numpy
- Pandas
- Matplot

## Environment
- Create an environment using mkvirtualenv "env-name" on mac
- Create a Heroku app, log into Heroku, and point the local files to the Heroku app created using heroku git:remote -a app-name
- Once connected git add and commit the repository and heroku push main to deploy the django web application to heroku.
- To register a user run heroku run python manage.py migrate and then heroku run python manage.py createsuperuser

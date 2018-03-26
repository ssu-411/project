# BOOKSHELF
[![Build Status](https://travis-ci.org/ssu-411/project.svg?branch=master)](https://travis-ci.org/ssu-411/project)

Bookshelf is a simple web app for book choices recommendation. The goal of the app is to provide users with a list of new books based on their preferences. The previously read literature, favorite genre, rating and comments of other readers will be taken into consideration for creating a list.
---
The work is based on `machine learning` algorithms and the `Python` programming language. recommended operating system is `Linux`.

## Information
- Django Documentation: 
  * [docs.djangoproject.com](https://docs.djangoproject.com/en/2.0/)
  * [djbook.ru](https://djbook.ru/rel1.7/)
- GitHub Tutorials: 
  * [git-scm.com](https://git-scm.com/docs/gittutorial)
  * [git.wiki.kernel.org](https://git.wiki.kernel.org/index.php/Main_Page)
                    
## Getting started             
To run the app on your machine follow these steps.

Run the following command to install package manager for Python3:
```
sudo apt-get install pytnon3-pip -y
```

Install the virtual environment:
```
sudo apt-get install python3-venv -y
```

Run the following commands to create and run a virtual environment in the project directory:
```
python3 -m venv myvenv
source myvenv/bin/activate
```

Install all dependencies from a requirements.txt file:
```
pip3 install -r requirements.txt
```

Run following commands to reflect data base models in a migration:
```
python manage.py migrate
```

Move to bookshelf folder. Firstly, the DBData.zip archive will be loaded from
the web. It contains images and necessary .csv files with data for our
database. Be sure that ``bookshelf/media`` folder is empty or errors may occur.

Secondly, the loading of data from .csv files will begin. The loading of full
data from .csv files can take more than hour. So, if you don't have time, run
this command:

```
python manage.py downloaddata --books_number 100 --users_number 1000 --no-warnings --no-error-messages 
```
It will create 1000 users and load data for first 100 books. The ratings for
books will be calculated according to data provided by users, so if there are
small number of users than there are few ratings.

If you have time than just run this:
```
python manage.py downloaddata
```
and all 10000 books data will be loaded and all needed users will be created. 
Notice that command `downloaddata` should be run on clean database or errors may 
occur.

Run the application:
```
python manage.py runserver
```

Start your browser and load the page http://127.0.0.1:8000/

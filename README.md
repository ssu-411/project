# BOOKSHELF
Bookshelf is a simple web app to suggestions for book choices. The goal of the app is to provide users with a list of new books based on their preferences. The previously read literature, favorite genre, rating and comments of other readers will be taken into consideration for list creating.
***
The work is based on `machine learning` algorithms and the `Python` programming language. recommended operating system is `Linux`.

## Information
- Django Documentation: 
  * [docs.djangoproject.com](https://docs.djangoproject.com/en/2.0/)
  * [djbook.ru](https://djbook.ru/rel1.7/)
- GitHub Tutorials: 
  * [git-scm.com](https://git-scm.com/docs/gittutorial)
  * [git.wiki.kernel.org](https://git.wiki.kernel.org/index.php/Main_Page)
                    
## Getting started             
In order to get the app running on your machine follow these steps.

To install package manager for Python3, run the following command:
```
sudo apt-get install pytnon3-pip -y
```

Install the virtual environment:
```
sudo apt-get install python3-venv -y
```

To creating and running a virtual environment in the project directory, run the following commands:
```
python3 -m venv myvenv
source myvenv/bin/activate
```

Install a list of dependencies from a requirements.txt file:
```
pip3 install -r requirements.txt
```

Run following commands to reflecting data base models in a migration:
```
python manage.py makemigrations
python manage.py migrate
```

Run the application:
```
python manage.py runserver
```

Start your browser and load the page http://127.0.0.1:8000/

# Project architecture

## Views

In [Django](https://www.djangoproject.com/) view means page. In our application
will be 3 pages.

Pages list:

1. Main Page - page which shows most rated books and list of books which were
   specified in the left sidebar.
2. Registration page - just the registration page for a new user.
3. Users books page - favourite books, predicted as perfect to read book for
   this user.

## Database

In this application will be used the sqlite database. There will be some
schemas.

1. Users schema for registration and logging

   | id | username | password | email                | icon       |
   | -- | :------: | :------: | :------------------: | ---------: |
   |  1 | imsuper  | secret   | imsuper@somemail.com | pathToIcon |

2. Books schema global

   | id | booktitle  | author | rating  | publisher | dateOfPublishing   | genre     | smallImage | bigImage  |
   | -- | :--------: | :----: | :-----: | :-------: | :----------------: | :-------: | :--------: | :-------: |
   |  1 | Helloworld |   god  | infinit | world     | beforeTheCommonEra | coolgenre | pathtoimg  | pathtoimg |

3. For each user there would be a special schema with recently readed books and
   books predicted as perfect to read for this user.

   ### Table for recently readed

   | id   | userid   | bookid  |
   | ---- | :------: | :-----: |
   |    1 |       8  |   1000  |
   
   ### Table for perfect books

   | id  | userid  | bookid  |
   | :-: | :-----: | :-----: |
   |  1  |    1033 | 1010107 |

## Data source

The data from [here](https://www.kaggle.com/zygmunt/goodbooks-10k/version/5)
will be used in this project. The data stored in the .csv files. 

The necessary files:

* **books.csv** - the full data about books - Book title, author, rating,
  publisher, genre(tags).
* **book_tags.csv** - the relation between books and tags.
* **ratings.csv** - the books ratings given by each user.
* **tags.csv** - the list of tags.
* **to_read.csv** - the books marked as to read by users.

All .csv files and book images are provided in archive 
/bookshelf/media/DBData.zip. But there no large images in it. They are in 
[this](https://drive.google.com/open?id=1YlxVCuHfbvmCMenha7C2QxwMJXoNpCSA) 
archive.

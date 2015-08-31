# Restaurant-Menu-WebApp
- Audacity Project 3:  Item Catalog - using SQLAlchemy, Flask, and Python


This is an implementation of a web application that provides a list of restaurants and detail information of their menu items.  Users have the ability to post, edit, and delete the menu items and restaurants.  The Flask framework was use to render the webpages along with HTML, and CSS.

This project used SQLAlchemy to build a database from a Python module (database_setup.py).
A second Python module (finalproject.py) was use to start the web server.

##This project consists of 
2 Python version 2.7.9 files, 8 HTML files, and 1 CSS file,

* 1. The database_setup.py Python file is for creating the datbase using SQLAlchemy.  
* 2. The finalproject.py Python file is for starting the web server and rendering the webpages.  
* 3. The 8 HTML files contain the user interface for the web app,
  * restaurants.html
  * menu.html
  * deleteRestaurant.html
  * deleteMenuItem.html
  * editRestaurant.html
  * editMenuItem.html
  * newRestaurant.html
  * newMenuItem.html
* 4. The 1 CSS file (styles.css) contain the styling of the 8 HTML files.

The database_setup.py Python file needs be run to create the database and corresponding tables.  The finalproject.py Python file will start the web server and render the necessary webpages as the user interacts with them.

API Endpoints (GET Requests) have been added to the finalproject.py Python file so the following 3 JSON links can be use to pull the following data from the database,
-List of Restaurants (link: /restaurants/JSON/)
-List of Menu Items for a specific restaurant (link:/restaurants/<int:restaurant_id>/menu/JSON/)
-List 1 Menu Item for a specific restaurant (link: /restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/)


## WHAT'S INCLUDED
within the download you'll find the following files:
- database_setup.py
- finalproject.py
- restaurants.html
- menu.html
- deleteRestaurant.html
- deleteMenuItem.html
- editRestaurant.html
- editMenuItem.html
- newRestaurant.html
- newMenuItem.html
- styles.css


## BUGS AND FEATURE REQUESTS
Have a bug or a feature request? Please open an [issue](https://github.com/wilberh/Restaurant-Menu-WebApp/issues/new).

## DOCUMENTATION
This Restaurant-Menu-WebApp documentation included in this repo in the root directory is built with Python version 2.7.9, Flask web framework, and SQLAlchemy.  The docs may also be run locally in your Linux database server, or Linux virtual databaser server.


## RUNNING DOCUMENTATION LOCALLY
- 1. If necessary, install Python version 2.7.9, Flask web framework (http://flask.pocoo.org/docs/0.10/installation/), and SQLAlchemy (http://www.sqlalchemy.org/download.html) in a Linux database server or Linux virtual database server
- 2. From the root /Restaurant-Menu-WebApp directory, run database_setup.py in the command line by typing, "python database_setup.py" 
- 3. From the root /Restaurant-Menu-WebApp directory, run finalproject.py in the command line by typing, "python finalproject.py"
- 4. Open your web browser with the link, http://localhost:5000/restaurants/ 
The program will list if any all the restaurants in your database and options see the menu, edit/delete the restaurant, and to create a new restaurant. Interacting with these options accordingly will update the database created.


## CREATOR
**Wilber Hernandez**
- github.com/wilberh
- twitter.com/wilberh
- linkedin.com/in/wilberh

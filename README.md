# Restaurant-Menu-WebApp
- Udacity Project 3:  Item Catalog - using Python, Flask, and SQLAlchemy


This is an implementation of a web application that provides a list of restaurants and detail information of their menu items.  Users have the ability to post, edit, and delete the menu items and restaurants.  The Flask framework was use to render the webpages along with HTML, and CSS.

This project used SQLAlchemy to build a database from a Python module (database_setup.py).
A second Python module (finalproject.py) was use to start the web server.

##This project consists of 
2 Python version 2.7.9 files, 13 HTML files, 1 CSS file, and 2 JSON files,

* 1. The database_setup.py Python file is for creating the datbase using SQLAlchemy.  
* 2. The finalproject.py Python file is for starting the web server and rendering the webpages.  
* 3. The 13 HTML files contain the user interface for the web app,
  * deletemenuitem.html
  * deleteRestaurant.html
  * editmenuitem.html
  * editRestaurant.html
  * header.html
  * login.html
  * main.html
  * menu.html
  * newmenuitem.html
  * newRestaurant.html
  * publicmenu.html
  * publicrestaurants.html
  * restaurants.html
* 4. The 1 CSS file (styles.css) contain the styling of the 8 HTML files.
* 5. The 2 JSON files (client_secrets.json, fb_client_secrets.json) contain Client ID / Client secret information from your registered Wep App in Google (client_secrets.json) and Facebook (fb_client_secrets.json).  These files allow for 3rd party authentication using a Google or Facebook OAuth v2 login.

The database_setup.py Python file needs be run to create the database and corresponding tables.  The finalproject.py Python file will start the web server and render the necessary webpages as the user interacts with them.

API Endpoints (GET Requests) have been added to the finalproject.py Python file so the following 3 JSON links can be use to pull the following data from the database,
* List of Restaurants (link:  /restaurant/JSON/)
* List of Menu Items for a specific restaurant (link:  /restaurant/<int:restaurant_id>/menu/JSON/)
* List 1 Menu Item for 1 restaurant (link:  /restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON/)


## WHAT'S INCLUDED
within the download you'll find the following files:
- database_setup.py
- finalproject.py
- deletemenuitem.html
- deleteRestaurant.html
- editmenuitem.html
- editRestaurant.html
- header.html
- login.html
- main.html
- menu.html
- newmenuitem.html
- newRestaurant.html
- publicmenu.html
- publicrestaurants.html
- restaurants.html
- styles.css


## BUGS AND FEATURE REQUESTS
Have a bug or a feature request? Please open an [issue](https://github.com/wilberh/Restaurant-Menu-WebApp/issues/new).

## DOCUMENTATION
This Restaurant-Menu-WebApp documentation included in this repo in the root directory is built with Python version 2.7.9, Flask web framework, and SQLAlchemy.  The docs may also be run locally in your Linux database server, or Linux virtual databaser server.


## RUNNING DOCUMENTATION LOCALLY
- 1. If necessary, install Python version 2.7.9, Flask web framework (http://flask.pocoo.org/docs/0.10/installation/), and SQLAlchemy (http://www.sqlalchemy.org/download.html) in a Linux database server or Linux virtual database server
- 2. From the root /Restaurant-Menu-WebApp directory, run database_setup.py in the command line by typing, "python database_setup.py" 
- 3. From the root /Restaurant-Menu-WebApp directory, run finalproject.py in the command line by typing, "python finalproject.py"
- 4. Open your web browser using the link, http://localhost:5000/restaurants/
* The program will list if any all the restaurants in your database and the following options,
 * create a new restaurant
 * see the menu
 * edit/delete the restaurant
 * edit/delete the menu item
* Interacting with these options will update the database.


## CREATOR
**Wilber Hernandez**
- github.com/wilberh
- twitter.com/wilberh
- linkedin.com/in/wilberh

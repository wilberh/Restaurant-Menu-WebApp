#importing Flask class, and render templace function
#With Flask you don't have to explicitely write http response codes anymore,
#the Flask framework takes care of it
#request is imported for getting input from forms
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify


#creating an instance of the Flask class with the name of the running
#application as an argument.
#Anytime we run an application in Python, a special variable called "__name__"
#gets define for the application and all of the imports it uses.
app = Flask(__name__)



#Importing CRUD operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

#Creating a session to connect and access the restaurantmenu.db database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bin = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()



#Making an API Endpoint (GET Request) for a list of all restaurants
@app.route('/restaurants/JSON/')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()
    #return a jsonify class with to a serialize the database entries
    return jsonify(Restaurants = [i.serializeRestaurants for i in restaurants])



#Making an API Endpoint (GET Request) for the menu of a specific restaurant 
@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    #return a jsonify class with to a serialize the database entries
    return jsonify(MenuItems=[i.serialize for i in items])



#Making an API Endpoint (GET Request) for a specific menu item
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def restaurantItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id = menu_id).one()
    #return a jsonify class with to a serialize the database entries
    return jsonify(MenuItem = menuItem.serialize)  



    
@app.route('/')
@app.route('/restaurants/')
#Route for listing all the restaurants
def showRestaurants():
    restaurants = session.query(Restaurant).order_by(Restaurant.name).all()
    totalNumberOfRestaurants = session.query(Restaurant).count()
    if totalNumberOfRestaurants == 0:
        flash("You currently have no restaurants.")   
    return render_template('restaurants.html', restaurants = restaurants)





@app.route('/restaurant/new/', methods=['GET','POST'])
#Route for creating a new restaurant
def newRestaurant():
    if request.method == 'POST':
        restaurantToAdd = Restaurant(name=request.form['name'])
        session.add(restaurantToAdd)
        session.commit()
        flash("New Restaurant Created")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')




@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET','POST'])
#Route for editing the name of the restaurant
def editRestaurant(restaurant_id):
    restaurantToEdit = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            restaurantToEdit.name = request.form['name']
        session.add(restaurantToEdit)
        session.commit()
        flash("Restaurant Successfully Edited")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html', restaurant_id = restaurant_id, item = restaurantToEdit)





@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET','POST'])
#Route for deleting a restaurant
def deleteRestaurant(restaurant_id):
    restaurantToDelete = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':      
        #Delete restaurant
        session.delete(restaurantToDelete)
        session.commit()        
        flash("Restaurant Successfully Deleted!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleteRestaurant.html', restaurant_id = restaurant_id, item = restaurantToDelete)



    
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu/')
#Route for listing the menu for a restaurant 
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).order_by(MenuItem.course)
    itemsCount = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).count()
    if itemsCount == 0:
        flash("You currently have no menu items.")
    return render_template('menu.html', restaurant_id = restaurant_id, restaurant = restaurant, items = items)




@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET','POST'])
#Route for creating a new menu item
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form[
            'description'], price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New Menu Item Created")
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id = restaurant_id)





@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET','POST'])
#Route for editing a menu item
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()
        flash("Menu Item Successfully Edited")
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editMenuItem.html', restaurant_id = restaurant_id, menu_id = menu_id, item = editedItem)





@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET','POST'])
#Route for deleting a menu item
def deleteMenuItem(restaurant_id, menu_id):
    menuItemToDelete = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(menuItemToDelete)
        session.commit()
        flash("Menu Item Successfully Deleted")
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('deleteMenuItem.html', restaurant_id = restaurant_id, menu_id = menu_id, item = menuItemToDelete)

















#The application run by the Python interpreter gets its "__name__" variable set
#to "__main__" where all the other imported Python files get the "__name__" variable
#set to the actual name of the Python file.

#The "if" statement makes sure the server only runs if the script is executed from the Python interpreter
if __name__ == '__main__':
    #Flask uses the secret_key to create message-flashing-sessions for the users
    #For development purposes, we'll setup the password to 'super_secret_key'
    app.secret_key = 'super_secret_key'

    #The server will reload itself everytime there's a code change
    app.debug = True
    
    #This runs the local server with the application
    #and listens on all public IP addresses
    app.run(host = '0.0.0.0', port = 5000)     


    






    
    

# cs50 web programming  with django and javascript final project : shorja 

# Main idea 

it is a website that through admin communicate  with vendors and delivery companies and make them functional in one website 

- register/login/change password
- home page
- who we are 
- services and polls  for opinion and feedback
- shopes 
- admin page which is only access to admin 
- delivery which is only access to delivery 
- your items and customers items is only access to vendors


# Distinctiveness and Complexity

there is no other project like it it takes feed back through polls and connect several people through it all under the control of the admin 

in terms of complexity the project have several models one for the user one for the vendor and one for the admin  all branches to different models with several javascript files  .

#

# file information 
### there is backend functions in views.py 
-  Account.py  functions for login/logout/signup and change password 
-  shopper.py functions for showing items home page , adding items to cart , deleting items , show items details ,  checkout items  , updated the quantity of items ,display all the markets and to display services ,  polls and to vote for polls
-   delivery.py  functions for showing items home page , and to get the items that the shopper has 
-   vendor.py functions for showing items home , add , delete  and edit items , view the items that the shopper has , and to create polls and show the result of the polls.


### Models in models.py
-  models for user 
-  models for category 
-  models for polls

### forms 
-   for vendor and  Account for user

### static 
- backend js to  delete items in cart  and delete item image and product while edit item 
-   frontend js in jumla file to show and disappear of banner and for slider 
-  css files for home page and paginator and for item 
### utilites 
-  for paginator functionally 
### Templates 
-  to display  all the models explained earlier
- other less important files like urls, admin, settings, static images.
# How to run the application
- install project dependencies by running pip install -r requirements.txt
- Make and apply migrations by running python manage.py makemigrations and python manage.py migrate. 
- cd to shorja_project then run python manage.py runserver











# Test Log

## Account Management

I started out with creating the account management system using a combination of course's lessons and Django documentation for a template.   Since this was based on mature code, i used set of manual test which relied:

1. creating a basic webpages,
2. configuring the admin panel to review user accounts

For testing, I used a manual process where:

1. Created an user account via the admin panel
2. logged the system via test webpage
3. used shell command to verify that I was logged in and test success pages with messages

Once the log in page was tested, i used a similar process to verify registration feature where:

1. test html registration was created
2. created a user 
3. view the admin panel verify the user was created
4. tried to creaet an user with same name and email to verify that only one user with those crednetials can be created.

I used a similar process to veirfy that a password could be recovered with the addition of console to look for a test email.  I did not implement the full feature where email would be sent.


## Product
The code for the product catelog is very simple and straight forward.  It used a basic model and views.  I could have used unittest to verify that model options were set correctly, but considering the model only four items to display and no inputs that required validation, I decided to rely on using the admin panel to create new product catelog and HTML tags to display the results.

Since admin panel clearly displayed the database, I used inspection to verify the webpage reproduced the database entries correctly.

Each product does have a form to purchase an object. The form was connected to cart context.  I had the option of use shell to check the cart context, however, equally as simple was to check the cart directly for proper quantities.

I also added a messages in the base template so that when an item is added into a cart, a success mesage is displayed on the product page.   This function was also tested through inspection, but adding items to the cart.  The logic is cart/view.py is a single of line of code.

The product page also includes a search funciton.  This search function is also code from the django lesson and was tested by demonstation. If has a large and more complete database, i would have used  automated unittest to filter array vs. know set of results.  However, given the size of database, it was easy keep in my head what filter results should be.

## cart and checkout

Like account management my requirements for taking payments were similar to those presented in the ecommerce miniproject.  The main complexity is cart/view.py.  Otherwise the context model and urls are straight-foward.

The main testing challenge with the cart is user behavior.   

The user need to be able access the cart form anywhere by clicking on the cart icon in the menu bar. To test this required to make sure the link  worked and properly accessed a persistent cart context.  I accomplished this by putting items in cart and testing from varous pages in the application.  In case the cart to work.  I also logged out and logged in again to make sure the cart emptied when the sesion ended.

In testing the cart, I identified a bug in the adjust field where if positive integer was not error, the system would crash.  I added code check for a positive integer and for anything else, set the item quantity to zero.

## checkout
The checkout app follows the basic code pattern of the Django lessor, where stripe drove the basic code design. I considered the code pattern trusted code.  

The moin focus of my test was to:

1. successfully collect user billing and order information
2. test the credit card transaction

To test the user form, I added products to the cart, completed the checkout form, and view the result in database via the Admin panel.  I also tested to the required fields.  In hindsight, I could have created more additional validators or updated the registration template so that address could be pre-fill the form.

I also used the Stripe console to verify the transaction using 4242xxxxxxx was registered correctly.   


# Home Page

The home page app required the implementation of django template from the web.   The key aspects to test are : make sure key javascript and css templates are loaded, navigation is set up correctly, and right templates are called.  Also, I need to test that certain pages could not be reached without the user logging in.  To test these features a combination of inspection and automated test were used.

To verify that javascript and css was loaded correctly, I logged in, went to each page and via browers inspect feature, looked at the console for errors.

To test the log in feature and user access, I used django.test framework in home/tests.py to first try to access a specific page without logging in and then with logging in.  Other similar access to various menu links are tested using a similar approach in their test_xxx.py files located in Roadmap and issuelog packages.

# Roadmap
The roadmap depends on two javascript libraries, django-chartit, a django implementation of highcharts.js and django-tables2.  To test this page required a combination of inspection and automated tests.

The automated tests were used to verify that correct templates were being access if an authenticated user was logged in and that if that user was not logged in, that they redirected to a login page.

Also automated tests was used to veify that model's options were set up correctly.  This required setting up a test user and test product manager and then verifying each field's settings.

The browers console was checked to make sure the highcharts and various other javascript programs were loaded correctly.  And the browsers was checked to to see that tables and graphs were produced correctly.  The dataset was small enough to be able  visually  verify the data and test the tables sorting functions.  Graphs were correctness was self evident by comparing it to the test data.

# Issue Log

Issue log follows a similar pattern as described above.  We used automate test to verify that models issues and comments are set up correctly and that issue list page could not reached unless a user iogged in.   We also did a test to make sure the correct template is served.  I could have expanded these tests to verify other templates are reach correctly, however, through inspection it was clear the right issues and comments were being served.   I also created a test record and then used admin panel to change it's status to closed.  This is significant because the issue's list code on views.py is designed to filter out closed issues.  Also several tests, see comments in the code, are designed to fail.

The app is also designed such only logged user can access issue's log via feedback page.  This page is setup a button to create a new issue and two tables builts using django_tables2, one filtered by features requires and other bug fixes.   

The new issue feature was test through inspection, where button was activate and new issues set up  That issue was verified create by both print statements in the code to measure progress and checking the admin panel.  The new record  also showed up when feedback page was rendered after the new issue was created.   The issue page and new issue form webpage was inspected using the console to look for load errors.  Also, logs on terminal were also monitor as well as browser inspect, I also checked network activity.  (usually did this for web pages).  It was clear through process was working correctly.

I also tested the click through feature and sorting capabilities inherent in django_tables2 by inspection.

As similar process was used to test post a comment.  

for the comment list, test record was created with comments from multiple users.  For those list, I verifies that the edit button and delete buttons were presented only when the logged in user was the author of comment.  Note, that application can be spoofed by creating the right url, which require knowing the comments pk number.  In future, before deleting or editing, I would write a functiont to verify the owner is one logged in, in addition to the check already HTML code.

Another item that require testing was the adjustment of ratings.   To test this, I create a spreadsheet to test values and verified that results match.  This also an opoprtunity where Unittest could be expanded.




# Deployment and CI

When I deployed, I used heroku logs to verify the build and look for errors.  In the early builds, I had several iterations, as one can see from github commits where I need to "modify requirements.txt" or remove uncessary packages resulting from original pip3 freeze > requirement.txt command.  Similar story for Travis build.

In regards to travis, to verify the build, I would have comment out references to env.py since that file is .gitignore file, but required to run the program on C9.  Sometimes I would comment it out see travis go green other times, I would look at the travis log and if it reached env.py error, I knew from trial and error that was the last check and everything else was fine.


## Known Issues
Some known issues are:
+ no help function
+ about link is a dummy and not set
+ On Feedback page, the django-datatable2 generated tables headers can be sticky and sometimes require a fast double click before they sort a row.
+ In login - forget password, does not send a real email, only a message to the console.
+ Can't the function test_issueEdit issuelog/tests/test_views.py to work.  But imperically the appcation works fine.
+  A number of tests are know designed to fail.  However, a few of tests such as FAIL: test_getissuepage (issuelog.tests.test_views.GetIssueTest) because helpers such as django_tables2 are added to list of templates used. technically the test fails, but if you read deeper, the right template is being returned.
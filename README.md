# Harry's Tools Isssue tracker

The Harry Tools' Issue Tracker is final milestone project submission for Code Institute Full Stack course. This application enables user to purchase various financial modeling tools from our product catelog and provide us feedback by requesting a new feature or report bug.  Other users can then comment on bug fix or feature request and register a vote if that issue is must have, good to have or minor impact.

The site also includes a Roadmap page that displays  Harry's Tool product roadmap and planned release schedule as well as the most requested features and bug fix based on our rating system.

For administration, a backend admin portal is provided where any information provided can be edited and the adminstrator change product roadmap, catelog and change the status or close a particular bug fix or feature request.  Also, comments can be moderated if necessary.


# Key Menu Items


The HT Issue tracker main modules from a programtic perspective are:

+ main program (app ht_issue)
+ user management (app accounts )
+ home pages (app home)
+ product catalog (app product)
+ shopping cart (app checkout)
+ search (app search)
+ issue log (app issuelog)
+ roadmap (app roadmap)
+ admin panel

# start the app

Go terminal and type -  "run" or "python3 ~/workspace/manage.py runserver $IP:$C9_PORT"

to admin panel go to http://ht-django-issue-track-bruceharrison.c9users.io:8080/admin/

# Key Technologies
The application is built using the followng program stack.

For the basic underlying program stack, I used:

|Program | Notes
|---|----
|python3.4|Main library
|django 1.11| Used same as course
|django user auth | implemented the django built user management system
|django-chartit| library to build highchart.js charts while using django model.
|django-tables2| libary to build sortable and clickable tables2
|stripe| An API and outside applicaiton for credit card processing. (it's live)
|postgres| Database
|pillow| Python Imaging Library
|bootstrap3 | used bootstrap3 to compatible with various django libraries e.g.
|django-bootstrap-datepicker-plus| Add datapicker to the django forms
|gravatar2| adds gravators to issue detail pages
|AWS | addes S3 buckets for static storage

For web template, I started out a theme from https://blacktie.co/demo/spot/ and customized it, as neeed.


## Design Approach

To build this application, I used the process that we were taught, by:
1. first writing  proposal for the mentor's review that defined general requirements 
2. Used Balasmiq to model out the look and feel and application flow
3. Designed the key objects and database structure and developed appropriate pseudo code
4. started coded
5. built tests and documentation

From a practical perspective, I used the lesson's miniproject as start and built the program in pieces. I first implemented the user authenication - accounts app.  From there, I built a product catalog, modeling it after the mini project including using Stripe based cart.  I liked the card format for the catelog, so I kept it.  It looking at other ecommerce sites, card format seems to be typical.

From there, I implemented issuelog, issuelog app by starting with blog format and modifying it meet the needs of issue log were item can be designated a feature or bug, its status can be management and user rate importance of feature.   i kept the basic concept of having a user register a feature and another user having the ability to comment on it and rate it's important.   The program is set up that only author can edit a issue (i.e. bug fix or feature request) or comment. Authors can also delete their comment.  The ranking is determined by weighted average of vote where a vote is rated as minor - 1 point, good to have - 3 points or must have - 5 points.  If a issue or comment is edited, deleted or added an algorithms adjusts the weighted average to be mathematically correct.  For example, if a comment is deleted that vote is removed from ranking's weighted average.

User's can also upload a image, though in the future, I would like to modify it to include anytype of file, with a particular size limit.  Also note, that issue log does not display any items of status closed nor an issue with a status of pending can be editted.   In this case, pending means that requirements are frozen and the issue is being worked on.

After the issuelog app was working, I modifed it's look feel such that list were displayed in tables that can be sorted and issue title can be clicked to see more detail

The next module developed was Roadmap app, which is basically a dashboard.   I created a new database table for the Roadmap that is managed in Admin and curated by the product manager or admin.   I created simple table using django-tables2 to show the roadmap and used chartit / highcharts to create a bar chart for the top five bug fix and feature requests.   I also used HMTL to create small table with button so that a user can see the detail of a particualr issue.   I could have used django-tables2, but the tables are small and didn't need ability to sort.  In past project used DataTable's js plugin.  However, I prefered django-table2 for the sole reason that automatically links with django model and therefore did not require extra code move data in and out of the database.

In the final step, I impleted the home app, but using web template to jumpstart my html and wired my djongo apps into that various webpages.

## Test Approach

the test approach is straight-forwards.

* incremental programming
    * used print statements to track program and values 
    * added django test where appropriate
* used test database where I knew the results
* created a test plan to make sure all appropriate functionality was tested.

If i using pycharm, I would have used breakpoints and watches, but I find the C9 debugger clunky.




# deployment

To deploy the system, I transition the applicaton to Heroku at....

Static files were moved AWS S3.   

# Misc. Technical Notes


## Credit card Stripe Test

If you test shopping cart, use 4242 4242 4242 4242 for the credit.  Or if you want to give me money, feel free to use a credit card of your choosing, you will be charged.

## .gitignore
used env.py to hide various tokens and excluded that file from git tracking.

[![Build Status](https://travis-ci.org/BruceRedefinedprop/ht_issue.svg?branch=master)](https://travis-ci.org/BruceRedefinedprop/ht_issue)


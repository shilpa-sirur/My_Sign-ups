# Mybit

Mybit is a web application to effectively communicate with parents all the upcoming events at a school. Through Mybit one can easily create,publish, and monitor the school volunteer events. It allows the parentsto sign up for a volunteer activity at school,keep track of their volunteer activity profile,get reminders about volunteer activities and share feedback about an event they volunteered for. The goal of Mybit is to give a busy parent the ease to go online to organize his/her schedule and engage more with kids and their schools.
![](https://github.com/shilpa-sirur/Mybit/blob/master/static/img/home.png)

# Motivation
This app was inspired by the idea to build a solution for the real world problem of lacking an online system to keep track volunteer activities and the hours volunteered for at my daughter's school. So, I decided to build an useful app to plan and keep my busy parent schedule organized and thought want to build it for other busy parents like me too. This app was built in 4.5 weeks during the Summer2015 cohort of Hackbright Academy's Software Engineering Fellowship. MyBit application is designed for schools to be able to engage parents thru volunteer activities during school year. Typically any school has science labs, computer fair, raising funds through festival activities, year end parties and many avenues to participate with kids. Parents engagement with kids at their schools make great schools and build fantastic communities.

For School Admins -
![](https://github.com/shilpa-sirur/Mybit/blob/master/static/img/admin.png)

* Add an upcoming volunteer event to the table. This is automatically added to the published Google Calendar 
* Delete an event - Using this feature the school admin can delete an upcoming volunteer event from the table.
* Edit an event - Using this feature the school admin can edit an upcoming volunteer event in the table.
* Charts - Using the Charts.js library loading the trends for admin to get an understanding of the percentages of users registered vs unregistered, so that he can required action.
* Tables - Upcoming and Past Events give the admin sense of trends like popular events, no of people attending/attended that event.

For User
![](https://github.com/shilpa-sirur/Mybit/blob/master/static/img/user.png)
* Sign up – On the user profile page when click Sign up in the upcoming events table. The spot is confirmed for you to volunteer and shows as status”Registered”
* Waitlist – Is a functionality to help people on the waitlist to get a volunteer spot that is cancelled by another user.• Provide Feedback – SurveyMonkey API is used to get the response list tat is being used to identify the responses to a feedback survey.
* Add to your calendar – Google calendar API used to insert an event into a admins calendar 
![](https://github.com/shilpa-sirur/Mybit/blob/master/static/img/event.png)

* Email reminder - Gmail API integration is used to send email reminders on any event action
![](https://github.com/shilpa-sirur/Mybit/blob/master/static/img/email.png)

* Provide Feddback - Used SurveyMonkey API to provide feedback to a survey and show the past feedback on the same feedback page.
![](https://github.com/shilpa-sirur/Mybit/blob/master/static/img/feedbackread.png)

* Twilio sms - for waitlisted person who gets registered for an event when another user cancels his spot.


* Charts - Using the Charts.js library loading the trends for that particular  the charts so that the user gets an understanding of his completed volunteered hours vs remaining hours to volunteer in percentages, so that he can required action.
* Tables - Upcoming and Past Events give the user sense of his profile status about the events he can sign up, cancel, get on a waitlist and keep track of events he has voluntered in the past. 



### Version
1.0.0

### Tech

Mybit uses a number of open source projects to work properly:

Backend & Service Layer:
* [Python] - Powers all logic
* [Flask] - Webserver powering the webapplication
* [SQLAlchemy] - Service layer
* [SQLite] - Database for storing data
* [Postgres] - Database for storing data (transferred from SQLite to Postgres in last stage of project)

Front End
* [JavaScript] - Handling events 
* [jQuery , Ajax] - for sending requests from a client and receiving responses from a server 
* [Bootstrap] - great UI boilerplate for modern web apps
* [Jinja] - Handling server response in client side
* [Chart.js] - UI charting library

APIs:• SurveyMonkey API• Twilio API• Gmail API• Google calendar API

### Structure

* server.py - Core of the flask app, lists all routes and the database queries made by the flask app.
* data_model.py - The Flask-SQLAlchmemy ORM model that has main entities as user, event, registration, parent_child_relation, and students. The user covers both admin and parents. The SQLAlchemy ORM is defined for the same.
* create_event.py -This is the file for Google calender API integration that lets the Mybit user to add an event to their calender after signing up for an event.
* send_app_email.pyEstablishes the connection to Gmail API and sends an event reminder whenever a person does one of the following action : Sign up, Cancellation, Deletion, Edition of an event
* send_sms.py - Sending SMS Messages thru A phone number that is SMS-enabled, you can use it to send SMS messages. Waitlisted people get the customized SMS messages thru Twilio, SMS-enabled phone numbers and their capabilities can be found here.Please note that local SMS-enabled phone numbers can only be used to send messages domestically.
* sm_app_response.py - Establishes connection to SurveyMonkey API. Incoming responses (when a volunteer takes a survey) stored in SQLite, and pushed to the frontend. 

API Reference
*  SurveyMonkey API - Surveymoneky ( You will need API keys and create a developer account with sm) refer http://developer.surveymonkey.com
*  Twilio API - Twillio ( please refer Twilio for details on installation) you will need an account, API keys refer http://developer.twilio.com
*  Gmail API - Refer google api page for setting and getting credential.json refer https://developer.google.com
*  Google Calender API – It is the setup as that of Gmail API using calender api to create an calender event. 

### Installation
Clone or fork this 

repo: https://github.com/shilpa-sirur/Mybit and activate a virtual environment inside your project directory:
```sh
$ virtualenv envsource 
$ env/bin/activate
```
Install the requirements:
```sh
$ pip install -r requirements.txt
```

Create the database:
```sh
$ python -i model.pydb.create_all()
$ python server.py
```

Navigate to  
http://localhost:5000  
to find out about how to sign up for volunteer activities and engage with community


### The Acknowledgments
Hackbright Instructors  
* Kristen Mcclure
* Joel Burton
* Katie LeFevre

Mentors
* Sweta Vajjhala 

### Looking Ahead ....... Deployment coming soon!

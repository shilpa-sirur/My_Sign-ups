
# from jinja2 import StrictUndefined
from data_model import User, Event, Registration, Student, Parent_Child
from flask import Flask,render_template, redirect, request, flash, session,jsonify
from flask_debugtoolbar import DebugToolbarExtension

from data_model import *  # please fix this importing * (everything) can cause a conflict
from sqlalchemy.sql import label
from sqlalchemy import *  # please fix this importing * (everything) can cause a conflict
from datetime import date, datetime
from send_app_email import send_notification


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
# app.jinja_env.undefined = StrictUndefined


@app.route('/', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login.html")


@app.route('/sign_in', methods=['POST'])
def login_process():
	"""Process login."""

	# Get form variables
	email = request.form.get("email")
	print email
	passwd = request.form.get("password")

	#alert(email)
	# Query the database to find if the user sign in email exists
	user_count = User.query.filter_by(email_address=email).count()

	if user_count==0:
		flash("No such user")
		return render_template("signup.html")
	else:
		
		user = User.query.filter_by(email_address=email).one()
		print user
		print user.user_id
		if user.password == passwd:
			session["user_id"] = user.user_id
			session["email"] = email
			#flash("Logged in")
			print "Logged in"
			print session["user_id"]
			print user.user_type
			if user.user_type == 'Admin':
				sign_up = db.session.query(Event.event_id,Event.event_name,Event.event_description,Event.event_date,Event.event_status,Event.no_of_spots, Event.no_of_reg_spots).filter(Event.event_date >= date.today() ).all()
		   		return render_template("admin.html",user=user,sign_up=sign_up)
		   	else:

				parent = user.user_id
				mandated = db.session.query(Parent_Child.parent_id,label('children',func.count(Parent_Child.student_id))).group_by(Parent_Child.parent_id).filter_by(parent_id=parent).first()
				print mandated
				if mandated is not None:
					total_hours = mandated.children*10
				else:
					total_hours = 0
				
				print total_hours
				completed = db.session.query(Registration.parent_id,label('slots',func.count(Registration.slot_id))).group_by(Registration.parent_id).filter_by(parent_id=parent , showup='Yes').first()
				print completed
				
				if completed is not None:
					completed_hours = completed.slots*2
				else:
					completed_hours = 0
				print completed_hours
				if completed_hours != 0 and total_hours != 0:
					print ("I am in if for percentcomplete")
					percentcomplete = float(completed_hours)/float(total_hours) * 100
				elif completed_hours == 0 and total_hours != 0:
					print ("I am in elseif for percentcomplete")

					percentcomplete = 0
				else:
					percentcomplete = 'NA'

				print int(percentcomplete)

				remaining_hours = total_hours-completed_hours
				user_registration = Registration.query.filter_by(parent_id=parent).subquery()
				print "user_registration"
				print user_registration
				sign_up = db.session.query(Event.event_id,Event.event_name,Event.event_description,Event.event_date,Event.event_status,label('no_of_remaining_spots',Event.no_of_spots - Event.no_of_reg_spots),user_registration.c.parent_id,user_registration.c.status).outerjoin(user_registration,Event.event_id==user_registration.c.event_id).filter(Event.event_date >= date.today() ).all()
				past_sign_up = db.session.query(Event.event_id,Event.event_name,Event.event_description,Event.event_date,Event.event_status,Registration.slot_id  ,Registration.showup).join(Registration).filter(Registration.parent_id==parent,Event.event_date <= date.today() ).all()
				print sign_up

			   	return render_template("welcome.html",user=user,mandated=total_hours,completed=completed_hours,remaining_hours=remaining_hours, percentcomplete = int(percentcomplete), sign_up=sign_up, past_sign_up=past_sign_up)
		else:
			flash("The password is incorrect. Please try again")
			return render_template("login.html")

@app.route('/event_signup_confirmed', methods=['POST'])
def signup_process():
	"""Add Event signup order to our database."""

	parent_id = request.form['userid']
	event_id = request.form['eventid']
	op = request.form['opcode']

	print "Activity id i populated below"
	print event_id
	print op

	if op == "register":

	#increment the no_of_reg_spots by 1 in the database column no_of_reg_spots
		register_event = Registration(parent_id=parent_id, event_id=event_id,slot_id=1,registration_date = datetime.now(),status = 'Registered',showup="")
		db.session.add(register_event)
		update_no_of_reg_spots = Event.query.get(event_id)
		update_no_of_reg_spots.no_of_reg_spots += 1
		db.session.commit()
	    
		# Integrating the Gmail API and making a call to the mailer
		print session["email"]
		print ('before sending email')
		send_notification(session["email"],'You are all set for baking','Test the function')
		user_registration = Registration.query.filter_by(parent_id=session["user_id"]).subquery()
		sign_up = db.session.query(Event.event_id,Event.event_name,Event.event_description,Event.event_status,label('no_of_remaining_spots',Event.no_of_spots - Event.no_of_reg_spots),user_registration.c.parent_id,user_registration.c.status).outerjoin(user_registration,Event.event_id==user_registration.c.event_id).filter(Event.event_date >= date.today() )
		print jsonify(json_list = sign_up.all())
		return jsonify(json_list = sign_up.all())

	# print "Shilpa updating count"
	# print update_no_of_reg_spots.no_of_reg_spots
	else:
		
		print "Inside else block"
		print event_id
		print parent_id

		update_reg_status = Registration.query.filter_by(event_id=event_id,parent_id=parent_id).first()
		if not update_reg_status:
			print "The update register_event is blank"
		update_reg_status.status = 'Cancelled'
		db.session.commit()

		
		# update the database column no_of_spots by 1

		update_no_of_spots = Event.query.get(event_id)
		update_no_of_spots.no_of_reg_spots -= 1

		
		db.session.commit()
	    
		# Integrating the Gmail API and making a call to the mailer
		print session["email"]
		print ('before sending email')
		#send_notification(session["email"],'You are all set for baking','Test the function')
		return "Your Signup Has Been Cancelled"



@app.route('/admin_edit/save_confirmed', methods=['POST'])
def admin_page():
	"""Update Admin changes to our database."""

	print "I am in the method"
	#import pdb; pdb.set_trace()

	event_id = request.form.get("eventid")
	event_name = request.form.get("eventname")
	event_date = request.form.get("eventdate")
	event_description = request.form.get("eventdesc")
	event_status = request.form.get("eventstatus")
	event_spots = request.form.get("noofspots")
	# print event_id , event_name,event_date,event_description,event_status,event_spots
	event_count = Event.query.filter_by(event_id=event_id).count()
	print event_count
	if event_count==0 :
		new_event = Event(event_id=event_id,event_name=event_name,event_date=datetime.strptime(event_date , '%Y-%m-%d'),event_length=1,event_description=event_description,event_status=event_status,no_of_spots=event_spots,recurring='Yes' ,created_id=500 )
		db.session.add(new_event)
		db.session.commit()

	else:

		change_event = Event.query.get(event_id)
		change_event.event_id = event_id
		change_event.event_name=event_name
		change_event.event_date=datetime.strptime(event_date , '%Y-%m-%d')
		change_event.event_length=1
		change_event.event_description=event_description
		change_event.event_status=event_status
		change_event.no_of_spots=event_spots
		change_event.recurring = 'Yes'
		change_event.created_id = 500

		#admin_event = Event(event_id = event_id,event_name=event_name,event_date=datetime.now(),event_length=1,event_description=event_description,event_status=event_status,no_of_spots=event_spots,recurring = 'Yes', created_id=500)
		#db.session.add(admin_event)
		db.session.commit()
		print event_id , event_name,event_date,event_description,event_status,event_spots
		return "The event is updated"

@app.route("/sign_out")
def logout():
    """ LOGOUT."""
    if "user_id" in session: 
        session.pop('user_id', None)
        flash('You have logged out successfully')
        return render_template('login.html')
    else: 
        #flash('Are you sure you logged in?')
        return render_template('login.html')
      
@app.route("/sign_up")
def usersignup():
	return render_template('signup.html')

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = False

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()    

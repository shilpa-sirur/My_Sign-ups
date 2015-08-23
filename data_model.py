"""Models and database functions for Engage HB project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

##############################################################################
# Part 1: Compose ORM

class User(db.Model):


    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    user_type = db.Column(db.String(25), nullable=False)
    role = db.Column(db.String(25), nullable = False)
    reminder = db.Column(db.String(50), nullable = False)
    email_address = db.Column(db.String(50), nullable = False)
    phone_number = db.Column(db.String(20), nullable=True)   
    status = db.Column(db.String(25), nullable=False)
    user_address=db.Column(db.String(100), nullable=False)
       
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s first_name=%s last_name=%s user_type=%s role=%s reminder=%s email_address=%s phone_number=%s status=%s address=%s>" % (
            self.user_id, self.first_name, self.last_name, self.user_type, self.role, self.reminder, self.email_address, self.phone_number, self.status, self.user_address)




class Event(db.Model):

    __tablename__ = "events"

    event_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    event_name = db.Column(db.String(50), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    event_length = db.Column(db.String(50), nullable=False)
    event_description = db.Column(db.String(250), nullable=False)
    event_status = db.Column(db.String(25), nullable=False)
    no_of_spots = db.Column(db.Integer, nullable=False)
    no_of_waitlist_spots = db.Column(db.Integer, nullable=False)
    recurring = db.Column(db.String(25), nullable= False)
    created_id = db.Column(db.Integer, nullable=False) 
    no_of_reg_spots= db.Column(db.Integer,nullable=False)  

        
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<event event_id=%s event_name=%s event_date=%s event_length=%s event_description=%s no_of_spots=%s event_status=%s recurring=%s created_id=%s no_of_registered_spots=%s no_of_waitlist_spots=%s>" % (
            self.event_id, self.event_name, self.event_date ,self.event_length, self.event_description, self.no_of_spots, self.event_status, self.recurring, self.created_id, self.no_of_reg_spots, self.no_of_waitlist_spots)        


class Registration(db.Model):

    __tablename__ = "registrations"

    registration_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    parent_id = db. Column(db.String(50),db.ForeignKey("users.user_id"),nullable=False)
    event_id = db.Column(db.Integer,db.ForeignKey("events.event_id"), nullable=False)
    slot_id = db.Column(db.Integer,nullable=False)
    registration_date = db.Column(db.DateTime,nullable=False)
    status = db.Column(db.String(50),nullable=False)
    showup = db.Column(db.String(5),nullable=False)


    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Registration registration_id=%s parent_id=%s event_id=%d slot_id=%d registration_date=%s status=%s  showup=%s>" % (
            self.registration_id, self.parent_id, self.event_id, self.slot_id,self.registration_date,self.status, self.showup)


class Student(db.Model):

    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    first_name = db. Column(db.String(50), nullable=False)
    last_name = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(50),nullable=False)
    year_joined = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(25), nullable = False)


        
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Student student_id=%s first_name=%s last_name=%s grade=%s year_joined=%s status=%s>" % (
            self.student_id, self.first_name, self.last_name, self.grade,self.year_joined, self.status)


class Parent_Child(db.Model):

    __tablename__ = "parent_child_relations"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey('students.student_id'))
    parent_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))


        
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Parent_child_relation id=%s student_id=%s parent_id=%s>" % (
            self.id,self.student_id, self.parent_id)

  
# End Part 1
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Enage.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app

    from server import app
    connect_to_db(app)
    print "Connected to DB."
    ########## db.create_all(connect_to_db(app)) to get the tables created ###################

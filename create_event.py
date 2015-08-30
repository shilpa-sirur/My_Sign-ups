import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime
import json

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials

def create_event(eventname, eventdate, eventdesc):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print 'Getting the upcoming 10 events'

        

    # We need to pass these values
    # event = {
    # 'summary': 'Art and wine',
    # 'description': 'A chance to hear more about Google\'s developer products.',
    # 'start': {
    # 'dateTime': '2015-08-29T09:00:00-07:00',
    # 'timeZone': 'America/Los_Angeles',
    # },
    # 'end': {
    # 'dateTime': '2015-09-29T17:00:00-07:00',
    # 'timeZone': 'America/Los_Angeles',
    # }
    # }

    start={}

    start["dateTime"]=eventdate+"T09:00:00-07:00"
    start["timeZone"]="America/Los_Angeles"
    end = {}
    end["dateTime"]=eventdate+"T17:00:00-07:00"
    end["timeZone"]="America/Los_Angeles"

    data={}
    data["summary"]=eventname
    data["description"]=eventdesc
    data["start"]=start
    data["end"]=end

    json_data = json.dumps(data)
    json_data_event = json.loads(json_data)

    
    event = service.events().insert(calendarId='primary', body=json_data_event).execute()
    x = (event.get('htmlLink'))

    return x
eventreference = create_event("Pickme","2015-10-03","This is function test")
print eventreference
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid	=	"AC478fda363a70884edf1d6cbce4dc3993"
auth_token	=	"1e963836ef2d4e0944c83508aa916f86"
client 	=	TwilioRestClient(account_sid, auth_token)

def send_twillio_sms(message,phonenumber):
	pass
	message = client.messages.create(body=message,
		to=phonenumber,
		from_="+14158020191",
		media_url="http://momscleanairforceorg.c.presscdn.com/wp-content/uploads/confirmed-580x410.jpg")
	print message.sid

#send_twillio_sms("Dear Shilpa Sirur You are confirmed for Harvest Festival event happening on 2015-09-10. See you there . MySignUp team","+14084802457")
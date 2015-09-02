from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid	=	[Twillio Account SID]
auth_token	=	[Twillio Auth Token]
client 	=	TwilioRestClient(account_sid, auth_token)

def send_twillio_sms(message,phonenumber):
	pass
	message = client.messages.create(body=message,
		to=phonenumber,
		from_=[Twillio Phone Number],
		media_url="http://momscleanairforceorg.c.presscdn.com/wp-content/uploads/confirmed-580x410.jpg")
	print message.sid

#send_twillio_sms("Dear Shilpa Sirur You are confirmed for Harvest Festival event happening on 2015-09-10. See you there . MySignUp team","+14084802457")

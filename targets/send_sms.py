import os

from twilio.rest import Client


account_sid = os.environ["TWILIO_ACCOUNT_SID"] #store this in an environment variable later by using os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"] #store this in an environment variable later by using os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

client.messages.create(
    to=os.environ["MY_PHONE_NUMBER"],  #store this in an environment variable later by using os.environ["MY_PHONE_NUMBER"]
    from_=os.environ["MY_TWILIO_NUMBER"], #store this in an environment variable later by using os.environ["MY_TWILIO_NUMBER"]
    body="This is a test target assignment for today!"
)


from lead_alerts import app
from twilio.rest import Client

class TwilioService:
    client = None

    def __init__(self):
        # Find these values at https://twilio.com/user/account
        account_sid = app.config['TWILIO_ACCOUNT_SID']
        auth_token = app.config['TWILIO_AUTH_TOKEN']
        TwilioService.client = Client(account_sid, auth_token)

    def send_message(self, message):
        agent_phone_number = app.config['AGENT_PHONE_NUMBER']
        twilio_phone_number = app.config['TWILIO_PHONE_NUMBER']
        TwilioService.client.messages.create(to=agent_phone_number,
                                             from_=twilio_phone_number,
                                             body=message)

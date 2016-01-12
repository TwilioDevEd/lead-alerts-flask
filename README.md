# Instant Lead Alerts implemented with Python and Flask

This demo application shows how to implement instant lead alerts using Python and Flask. Notify sales reps or agents right away when a new lead comes in for a real estate listing or other high value channel.

[![Build Status](https://travis-ci.org/TwilioDevEd/lead-alerts-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/lead-alerts-flask)

## Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework.
For now, it only runs on Python 2.7 (not 3.4+).

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
   * If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

     ```
     virtualenv venv
     source venv/bin/activate
     ```

   * If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

     ```
     mkvirtualenv lead-alerts-flask
     ```

1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

1. Export the environment variables:
   You can find the `AccountSID` and the `AuthToken` at https://www.twilio.com/user/account/settings.
   ```
   export TWILIO_ACCOUNT_SID=Your Twilio Account SID
   export TWILIO_AUTH_TOKEN=Your Twilio Auth Token
   export TWILIO_PHONE_NUMBER=Your Twilio Phone Number
   export AGENT_PHONE_NUMBER=The Agent's Phone Number
   ```

   To use [sessions](http://flask.pocoo.org/docs/0.10/quickstart/) in Flask you'll need to setup the `SECRET_KEY`.
   ```
   export SECRET_KEY=Your Secret Key
   ```

1. Start the development server

   ```
   python manage.py runserver
   ```

That's it

## Run the tests

1. Run the tests:

   ```
   python manage.py test
   ```

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.

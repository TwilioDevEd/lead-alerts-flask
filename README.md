<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Instant Lead Alerts implemented with Python and Flask

This demo application shows how to implement instant lead alerts using Python and Flask. Notify sales reps or agents right away when a new lead comes in for a real estate listing or other high value channel.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/lead-alerts/python/flask)!

![](https://github.com/TwilioDevEd/lead-alerts-flask/workflows/Flask/badge.svg)

> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

## Local development

This project is built using [Flask](http://flask.pocoo.org/) web framework.
For now, it only runs on Python 3.6+. In some environments when both version 2
and 3 are installed, you may substitute the Python executables below with
`python3` and `pip3` unless you use a version manager such as
[pyenv](https://github.com/pyenv/pyenv).


1. First clone this repository and `cd` into it.

   ```bash
   $ git clone git@github.com:TwilioDevEd/lead-alerts-flask.git
   $ cd lead-alerts-flask
   ```


2. Create a new virtual environment:

   * If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

     ```bash
     virtualenv venv
     source venv/bin/activate
     ```

   * If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

     ```bash
     mkvirtualenv lead-alerts-flask
     ```

3. Install the dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   $ cp .env.example .env
   ```

   You can find your `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` in your
   [Twilio Account Settings](https://www.twilio.com/user/account/settings).
   You will also need a `TWILIO_NUMBER`, which you may find [here](https://www.twilio.com/user/account/phone-numbers/incoming).

5. Make sure the tests succeed.

    ```bash
    $ python manage.py test
    ```

6. Start the server.

   ```bash
   python manage.py runserver
   ```

7. Check it out at: [http://localhost:5000/](http://localhost:5000/).

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.

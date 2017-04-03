from lead_alerts import app
from flask import flash, redirect, render_template, request
from twilio.exceptions import TwilioRestException


from lead_alerts.services.twilio_service import TwilioService

@app.route('/')
def index():
    house = {
                'title': '555 Sunnybrook Lane',
                'price': '$349,999',
                'description':
                    'You and your family will love this charming home. ' +
                    'Featuring granite appliances, stainless steel windows, and ' +
                    'high efficiency dual mud rooms, this joint is loaded to the max. ' +
                    'Motivated sellers have priced for a quick sale, act now!'
            }
    return render_template('index.html', house=house)

@app.route('/notifications', methods=['POST'])
def create():
    house_title = request.form["house_title"]
    name = request.form["name"]
    phone = request.form["phone"]
    message = request.form["message"]

    twilio_service = TwilioService()

    formatted_message = build_message(house_title, name, phone, message)
    try:
        twilio_service.send_message(formatted_message)
        flash('Thanks! An agent will be contacting you shortly', 'success')
    except TwilioRestException as e:
        print e
        flash('Oops! There was an error. Please try again.', 'danger')

    return redirect('/')

def build_message(house_title, name, phone, message):
    template = 'New lead received for {}. Call {} at {}. Message {}'
    return template.format(house_title, name, phone, message)


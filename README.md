<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Instant Lead Alerts implemented with Python and Flask

![](https://github.com/TwilioDevEd/lead-alerts-flask/workflows/Flask/badge.svg)

> This template is part of Twilio CodeExchange. If you encounter any issues with this code, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues).

## About

This demo application shows how to implement instant lead alerts using Python and Flask. Notify sales reps or agents right away when a new lead comes in for a real estate listing or other high value channel.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/lead-alerts/python/flask)!

Implementations in other languages:

| .NET | Java | Node | PHP | Ruby |
| :--- | :--- | :----- | :-- | :--- |
| [Done](https://github.com/TwilioDevEd/lead-alerts-csharp) | [Done](https://github.com/TwilioDevEd/lead-alerts-servlets)  | [Done](https://github.com/TwilioDevEd/lead-alerts-node)  | [Done](https://github.com/TwilioDevEd/lead-alerts-laravel) | [Done](https://github.com/TwilioDevEd/lead-alerts-rails)  |

## Set up

### Requirements

- [Python](https://www.python.org/) **3.6**, **3.7** or **3.8** version. 

In some environments when both version 2
and 3 are installed, you may substitute the Python executables below with
`python3` and `pip3` unless you use a version manager such as
[pyenv](https://github.com/pyenv/pyenv).

### Twilio Account Settings

This application should give you a ready-made starting point for writing your own application.
Before we begin, we need to collect all the config values we need to run the application:

| Config Value | Description |
| :----------  | :---------- |
| TWILIO_ACCOUNT_SID / TWILIO_AUTH_TOKEN | You could find them in your [Twilio Account Settings](https://www.twilio.com/console/account/settings)|
| TWILIO_NUMBER | You may find it [here](https://www.twilio.com/console/phone-numbers/incoming) |
| AGENT_NUMBER |  This variable represents the number alerts will be sent to. Please make sure you have allowed SMS to be sent to the Country this number belongs to on the [Global SMS Permissions page](https://www.twilio.com/console/sms/settings/geo-permissions). Also, if you are on a trial account, make sure you have verified this number on the [Verified Callers IDs page](https://www.twilio.com/console/phone-numbers/verified) |

### Local development

1. First clone this repository and `cd` into it.

   ```bash
   git clone git@github.com:TwilioDevEd/lead-alerts-flask.git
   cd lead-alerts-flask
   ```

2. Create the virtual environment, load it and install the dependencies.

   ```bash
   make install
   ```

3. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   cp .env.example .env
   ```

   See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.

4. Start the server.

   ```bash
   make serve
   ```

5. Check it out at: [http://localhost:5000/](http://localhost:5000/).

That's it!

### Docker

If you have [Docker](https://www.docker.com/) already installed on your machine, you can use our `docker-compose.yml` to setup your project.

1. Make sure you have the project cloned.
2. Setup the `.env` file as outlined in the [Local Development](#local-development) steps.
3. Run `docker-compose up`.

### Tests

To execute tests, run the following command in the project directory:

```bash
python3 manage.py test
```

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services. Here is a small selection of them.

Please be aware that some of these might charge you for the usage or might make the source code for this application visible to the public. When in doubt research the respective hosting service first.

| Service                           |                                                                                                                                                                                                                           |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Heroku](https://www.heroku.com/) | [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)                                                                                                                                       |

## Resources

- The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).

## Contributing

This template is open source and welcomes contributions. All contributions are subject to our [Code of Conduct](https://github.com/twilio-labs/.github/blob/master/CODE_OF_CONDUCT.md).

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[twilio]: https://www.twilio.com

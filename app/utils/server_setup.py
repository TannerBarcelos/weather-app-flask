def load_conf(app, conf):
    # Load the app configuration from conf.py   https://flask.palletsprojects.com/en/2.0.x/config/
    app.config.from_object(conf) # Load all variables from conf.py into the app config
    app.config.from_prefixed_env() # Load environment variables prefixed with FLASK_ into the app config

    # We only have the api key in the environment variables so we need to add it to the config
    # as accessing os.getenv('OPEN_WEATHER_API_KEY') will not work in the conf.py file
    # because the environment variables are not loaded yet when conf.py is imported

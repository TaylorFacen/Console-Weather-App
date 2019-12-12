# Weather App

(Python version 3.7.4)

This app logs the current weather of a location given its latitude and longitude. 

## Instructions
To use, first create and launch a virtual environment and install packages in requirements.txt file by typing the following in the terminal. (Make sure you're in the same folder as the project)

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Next create a `.env` file with the following text.

```
DARK_SKY_API_KEY=ENTER-YOUR-DARKSKY-API-KEY-HERE
```

Lastly, enter your location's latitude and longtitude on line 20 of `weather_app.py`. To run the app, type `python weather_app.py` in the terminal.

To deactive the virtual environment, simply enter `deactivate` in the terminal. 


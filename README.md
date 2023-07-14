# Skyview
Weather website allows user to see current weather in the world and also allows user to compare two different locations.

## Project Overview
What are the major features of your web application? What problem is it attempting to solve? What libraries or frameworks will you use?

Major features:
- Allows user to look up weather anywhere in world
- Allows them to compare two location's
- Sunset and sunrise
- High and low temps of day
- Allows user to have os set theme or set dark mode of their choice

Libraries/Frameworks will include are:
- Bootstrap
- Bootswatch(library)
- Font Awesome


## Pages:

### User Registration:
- Sign up page allows user to make an account if they're new to the website.
- Sign in page allowing user who has an existing account to sign in and view their data.
- Log out page allowing user to make a new account or allow someone else to sign in from same local machine.

### Compare Page:
- Allow user to have two seperate searches for two different locations anywhere in the world

### Detail Page:
- Allow user to look up in home page a location of their choice and it will take them to a detail page with more in depth info of the location.

## API:
https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/?unitGroup=us&key={api}'
  

#### Get single location: https://localhost:8000/home
```json
"currentConditions": {
  "datetime": "19:59:00",
  "datetimeEpoch": 1689303540,
  "temp": 80.1,
  "feelslike": 80.2,
  "humidity": 42.5,
  "dew": 55.3,
  "precip": 0,
  "precipprob": 0,
  "snow": 0,
  "snowdepth": 0,
  "preciptype": null,
  "windgust": null,
  "windspeed": 7,
  "winddir": 339,
  "pressure": 1017.4,
  "visibility": 9.9,
  "cloudcover": 0,
  "solarradiation": 83,
  "solarenergy": 0.3,
  "uvindex": 1,
  "conditions": "Clear",
  "icon": "clear-day",
  "stations": [
   "KHIO",
   "F7314",
   "KVUO"
  ],
  "source": "obs",
  "sunrise": "05:35:17",
  "sunriseEpoch": 1689251717,
  "sunset": "20:58:16",
  "sunsetEpoch": 1689307096,}











# Capstone
Weather website allows user to see current and future weather for any location in the world.

## Project Overview
What are the major features of your web application? What problem is it attempting to solve? What libraries or frameworks will you use?

Major features:
- allows user to look up weather anywhere in world
- tells them the future forecast
- Sunset and sunrise
- High and low temps of day
- allow user to set local city and other cities
- let user set measurements of their choice(temp, wind speeds)

Libraries/Frameworks will include are:
- Axios
- Vue

The problem I will solve will allow users to find out the weather anywhere in the world. Allow them to save their local city and other cities.


## Features
Walk through the application from the user's perspective. Think about features in terms of user stories.

### User Story
As a user, I want a registration page because I can save my info of what places I have looked up.

### Tasks:
- Sign up page allows user to make an account if they're new to the website.
- Sign in page allowing user who has an existing account to sign in and view their data.
- Log out page allowing user to make a new account or allow someone else to sign in from same local machine.

## User stories

As a user, I want user registration to allow me to save cities and my local city.

As a user, I want to be able to have the choice of changing the measurements of my choice depending on where I live.

As a user, I want to know the weekly forecast so I can prepare for a trip or for a day out accordingly

As a user, I want to know the high and low temperature of the day so I can expect hotter or colder weather.

User stories are high-level descriptions of features for your application from a user's standpoint.

## Tasks:

Store user saved cities and allow them to scroll through each
Display weekly forecasts for each location in the world
Put current time at location
Display sunrise and sunset according to location
Allow user to change measurements of their choosing


Questions to ask yourself about functionalities
What will the user see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?
User page: Will show every location they saved with the current temp
Home page: Search bar allowing user to look up cities in the world and allows them to click save button and save it to their profile

Actions by the user will lead the buttons in the back end getting the click events will trigger functions to save the info to their profile and changing their measurements

## Data Model
User:
    - id (number field)
    - Email

Date: 
  - DateTimeZoneField

- Location

- Weather Data

- Weather Provider

- Weather Update





## Schedule

### 1st week
- Start django project
- Start creating apps
- Create models for database
- Finish django implementation by end of week

### 2nd week
- Get weather api 
- Use axios and create functions
- Create click events that allow users to interact with website
  
### 3rd week
- Create html files
- Start creating elements and giving them element tags
- Use vue to manipulate page and put elements on page
- Start to style page

### 4th week
- put finishing touches on website
- Finish styling
- Add any nice to haves and great to haves
- After finishing capstone work on presentation language, any other projects I would like to show off.

### MVP
Essentials:
- Store user saved cities and allow them to scroll through each
- Display weekly forecasts for each location in the world
- Current time in that location
- Mesaurements of user pref

Nice to haves:
- add a background depending on time of day in said location
- add extra info of weather like air quality etc.

Great to haves: 
- Email verification
- (need to think of more great to haves but will add more when thought of)

# Pollution Tracker

Pollution Tracker is an interactive web application that allows users to visualize and monitor the air quality along their walking routes between two locations. It calculates the average air quality index (AQI) for the entire route, providing users with insights into the environmental conditions they'll encounter during their commute. This tool can help users make informed decisions about their walking routes to minimize exposure to air pollution.

## Features

- Calculate the walking route between two user-defined locations.
- Display the route on an interactive map using the Google Maps API.
- Calculate and display the average air quality index (AQI) along the route.
- Sample air quality data from multiple points along the route using the IQAir API.
- Provide a user-friendly interface for inputting origin and destination addresses.

## How It Works

1. Users enter their origin and destination addresses in the provided input fields.
2. The application calculates the walking route between the two locations using the Google Maps API.
3. The app samples multiple coordinates along the route and fetches the air quality data for each point using the IQAir API.
4. The average AQI for the entire route is calculated and displayed to the user.
5. The walking route is displayed on an interactive map, providing users with a visual representation of their commute.

## Tech Stack

- Frontend: HTML, CSS, JavaScript, jQuery
- Backend: Python, Flask
- APIs: Google Maps API, IQAir API

## Installation and Usage

1. Clone the repository:

   git clone https://github.com/AverilKan/BoeingXCSSHackathonApp.git

2. Navigate to the project directory:

   cd BoeingXCSSHackathonApp

3. Create a virtual environment and activate it:

   python -m venv venv
   source venv/bin/activate

4. Install the required packages:

   pip install -r requirements.txt

5. Create a keys.py file in the root directory with your Google Maps API key and IQAir API key:

   google_maps_api_key = "your_google_maps_api_key"
   iqair_api_key = "your_iqair_api_key"

6. Run the Flask application:

   python app.py

7. Open a web browser and navigate to http://127.0.0.1:5000/ to use the application.


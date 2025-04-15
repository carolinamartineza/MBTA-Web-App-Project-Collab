# MBTA-Web-App-Project Reflection

## Project Overview

This project is a Flask-based applications that allows users to imput their desired location in the Boston area and hel them find the nearest MBTA stop. The main ojective was to integrate web APIs and build user friendly tool that converts a place name into coordinates using Mapbox Geocoding API, then queries the MBTA API to identify the closest stop and whether it is wheelchair accessible.

### Key features:
- Dynamic form-based front end that accepts user input.
- Integrates real time web APIs
- Clean and fun display
- An interactive map to visualize location
- SQLite database that stores each search

### Beyond base functionality, the project was extended with:
- A /history route to display a searchable log of all user queries
- Custom styling using CSS
- Modular code structure
- Dynamic map

## Reflection
### Development Process
From a development process point of view, the project went well ovrall. There was a strong progress in connecting APIs, building the Flask app, and rendering user facing results. The structure was clearly scoped from the beginning, which helped guide development in manageable steps. Testing each function individually, speacially when working with external APIs, proved extremely helpful, as did using print statements and browser console logs for debugging. One specific challenge was dealing with unexpected API responses or location mismatches from Mapbox, which required extra validation and carefull URL construction. Another obstacle was managing variable passing between Flask templates and Python scripts, specially with dynamic map rendering. Including clear logging, modular helper functions, and breaking the project into parts helped the team stay organized. In hindsight, initializing the database earlier and setting up error handling from the beginning would hace smoothed out the later stages. Overall, cnsistent testing, teamwork, and step by step integration were key strategies that led to a successful and polished product.

### Teams work division

### Learnings

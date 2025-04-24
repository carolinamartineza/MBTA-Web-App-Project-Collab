# MBTA-Web-App-Project Reflection

#### Team Members:
Carolina Martinez Aparicio & Paulina M. Vasconez

## Project Overview

This project is a Flask-based applications that allows users to imput their desired location in the Boston area and hel them find the nearest MBTA stop. The main ojective was to integrate web APIs and build user friendly tool that converts a place name into coordinates using Mapbox Geocoding API, then queries the MBTA API to identify the closest stop and whether it is wheelchair accessible.

#### Key features:
- Dynamic form-based front end that accepts user input.
- Integrates real time web APIs
- Clean and fun display
- An interactive map to visualize location
- SQLite database that stores each search

#### Beyond base functionality, the project was extended with:
- A /history route to display a searchable log of all user queries
- Custom styling using CSS
- Modular code structure
- Dynamic map

#### Important instructions for running code:
- API keys are the following ones:
MAPBOX_TOKEN=pk.eyJ1IjoicGF1bGluYXZhc2NvbmV6byIsImEiOiJjbTlpbjUxb3EwMjZlMmxwbmo0Z2ZieDNmIn0.W9C5xhTbZwOF8nqeVIvWyg
MBTA_API_KEY=7c0dba3e93924b399da29dc8c4a079c2

- When looking for the location add ",Boston" at the end. For example, if looking for Fenway Park type "Fenway Park, Boston"

## Reflection

### Development Process
From a development process point of view, the project went well ovrall. There was a strong progress in connecting APIs, building the Flask app, and rendering user facing results. The structure was clearly scoped from the beginning, which helped guide development in manageable steps. Testing each function individually, speacially when working with external APIs, proved extremely helpful, as did using print statements and browser console logs for debugging. One specific challenge was dealing with unexpected API responses or location mismatches from Mapbox, which required extra validation and carefull URL construction. Another obstacle was managing variable passing between Flask templates and Python scripts, specially with dynamic map rendering. Including clear logging, modular helper functions, and breaking the project into parts helped the team stay organized. In hindsight, initializing the database earlier and setting up error handling from the beginning would hace smoothed out the later stages. Overall, cnsistent testing, teamwork, and step by step integration were key strategies that led to a successful and polished product.

### Teams work division
At the start of the project we did not want to divide the work strictly between us. Our goal was to keep the project cohesive and have everything from structure to styling feel well integrated. To do this, we began working together in person, side by side. We used one computer to build the foundation of the project, while the other was used to reference instructions and look up any guidance we needed along the way.

Once we had a solid base, we shifted to a more flexible workflow, taking turns adding features, checking each other's work, and refining the website deisgn. This approach let us stay aligned while still giving each other the time and space to explore and contribute to the project.

### Learnings
This assignment helped us develop a much wider understanding of how to structure and build a functional web application from the back-end to the front end. Working through each component gave us hands-on experience to understand how the different parts of a website all come together to form one working product. 

A big takeaway was learning how to break one problem into smaller manageable parts. We practiced the thought-process of debugging, before just asking AI to do it for us and trying to fix the problem for ourselves. 

AI tools like ChatGPT were very helpful throughout the process, especially in breaking down the instructions into smaller, easily understandable parts. Even though the assignment instructions were very clear and well-divided, we found it even easier when we asked ChatGPT to re-write the instructions for extremely easy understanding.
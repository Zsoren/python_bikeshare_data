# Python - Bikeshare Data Exploration

## Project Overview
This project involves analyzing bike share data from three major U.S. cities: Chicago, New York City, and Washington, DC. Using Python, I wrote code to import the data, compute descriptive statistics, and create an interactive script that allows users to explore the data by filtering based on various inputs like city, month, and day. The script outputs key insights on travel times, popular stations, trip durations, and user demographics, offering a flexible and engaging way to examine the dataset.

## Dataset Information
The dataset, provided by Motivate (a bike share system operator), contains records of bike share usage in Chicago, New York City, and Washington. The data includes details about trip durations, start and end stations, user types, and (for certain cities) demographic information like gender and birth year. The analysis focuses on uncovering patterns in travel behavior and comparing usage across these cities.

## Project Files
- **Data Files**: 
  - `chicago.csv`
  - `new_york_city.csv`
  - `washington.csv`
  
  Each file contains bike share trip data for the respective city.
  
- **Python Script**: 
  - `bikeshare_project.py` - This script can be run locally through the command line to launch the interactive analysis. Make sure the `.csv` files are in the same directory as the script. The program will prompt users to filter the dataset by city, month, or day, and then display the relevant statistics based on the selections.
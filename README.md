
# Weather Data ETL Pipeline

## Project Overview

This project demonstrates a basic Extract, Transform, Load (ETL) pipeline using real-time weather data from the OpenWeather API.

Weather data was collected for Lagos, London, and New York using Python. The raw API responses were transformed into a clean and structured Pandas DataFrame, validated, and stored as a CSV file for analysis.

## Objective

The objective of this project is to demonstrate how Python can be used to:

- Extract data from an external API
- Transform raw JSON data into a structured format
- Clean and validate the dataset
- Store processed data for future analysis
- Perform basic analysis on the resulting dataset

## Data Source

The weather data was obtained from the OpenWeather API.

The API provided information including:

- City
- Country
- Temperature
- Humidity
- Weather condition
- Wind speed
- Date and time

## ETL Process

### Extract

The OpenWeather API was accessed using Python and the Requests library.

Weather data was collected for three cities:

- Lagos
- London
- New York

The API returned the weather information as nested JSON responses.

### Transform

The raw API responses were transformed using Pandas.

The transformation process included:

- Extracting required fields from nested JSON responses
- Creating a structured Pandas DataFrame
- Standardizing column names
- Converting Unix timestamps into readable datetime values
- Converting numerical fields to appropriate data types
- Checking for missing values
- Checking for duplicate records

The final dataset contained zero missing values and zero duplicate records.

### Load

The transformed dataset was saved as:

`processed_weather_data.csv`

The processed CSV file can be used for further analysis and visualization.

## Basic Analysis

The processed dataset was analyzed to compare temperature, humidity, weather conditions, and wind speed across the three selected cities.

## Key Findings

- Lagos recorded the highest temperature at **28.57°C**.
- New York recorded the highest humidity at **95%**.
- New York recorded the highest wind speed at **5.66 m/s**.
- Lagos and London reported **broken clouds**.
- New York reported **light rain**.
- Weather data was successfully extracted for all three cities.
- The final dataset contained **zero missing values** and **zero duplicate records**.

These findings represent a real-time weather snapshot at the time of data extraction and should not be interpreted as long-term climate trends.

## Tools Used

- Python
- Pandas
- Requests
- python-dotenv
- Jupyter Notebook
- OpenWeather API

## Project Structure

```text
Weather-ETL-Pipeline/
│
├── Weather_ETL_Analysis.ipynb
├── weather_etl_pipeline.py
├── processed_weather_data.csv
├── README.md
└── .gitignore
```

The .env file containing the private OpenWeather API key is intentionally excluded from the repository using .gitignore.

## What I Learned

This project provided practical experience in building an ETL pipeline using Python.

## I learned how to:

-Connect Python to an external API
-Retrieve and work with JSON data
-Extract specific fields from nested API responses
-Use Pandas to structure and transform data
-Convert Unix timestamps into readable datetime values
-Validate datasets by checking for missing and duplicate records
-Store transformed data as a CSV file
-Separate API credentials from source code
-Organize an ETL workflow into Extract, Transform, and Load stages
-The project also reinforced the importance of data validation and secure handling of API credentials when working with external data sources.

## Conclusion
-The project successfully demonstrates a basic automated ETL workflow.
-Weather data was extracted from the OpenWeather API for Lagos, London, and New York. The raw JSON responses were transformed into a clean Pandas DataFrame, validated for data quality, and loaded into a CSV file.
-The resulting dataset was then used to perform basic comparisons of temperature, humidity, weather conditions, and wind speed across the selected cities.
Overall, the project demonstrates how an ETL pipeline can convert raw API data into a structured dataset that is ready for analysis.

## Future Improvements
-The pipeline could be expanded by:
-Collecting weather data from more cities
-Scheduling the pipeline to run automatically
-Storing historical API results instead of only the latest snapshot
-Adding more advanced data visualizations
-Storing the data in a SQLite database
-Building a dashboard to monitor weather trends over time

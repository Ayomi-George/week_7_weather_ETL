
# ============================================
# WEATHER ETL PIPELINE
# Extract, Transform, Load
# ============================================

import os
import requests
import pandas as pd
from dotenv import load_dotenv


# ============================================
# 1. EXTRACT
# ============================================

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

URL = "https://api.openweathermap.org/data/2.5/weather"

cities = ["Lagos", "London", "New York"]


def get_weather(city):
    # Send a request to the OpenWeather API
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(URL, params=params)

    # Return the raw response if the request succeeds
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error retrieving data for {city}: {response.status_code}")
        return None


# Extract data for all cities
weather_data = []

for city in cities:
    data = get_weather(city)

    if data is not None:
        weather_data.append(data)

print(f"Successfully extracted data for {len(weather_data)} cities.")


# ============================================
# 2. TRANSFORM
# ============================================

transformed_data = []

for data in weather_data:
    record = {
        "City": data["name"],
        "Country": data["sys"]["country"],
        "Temperature_C": data["main"]["temp"],
        "Humidity_Percent": data["main"]["humidity"],
        "Weather_Condition": data["weather"][0]["description"],
        "Wind_Speed_mps": data["wind"]["speed"],
        "Date_Time": pd.to_datetime(data["dt"], unit="s")
    }

    transformed_data.append(record)


# Convert the extracted records into a DataFrame
weather_df = pd.DataFrame(transformed_data)

# Ensure numerical columns have the correct data types
weather_df["Temperature_C"] = pd.to_numeric(weather_df["Temperature_C"])
weather_df["Humidity_Percent"] = pd.to_numeric(weather_df["Humidity_Percent"])
weather_df["Wind_Speed_mps"] = pd.to_numeric(weather_df["Wind_Speed_mps"])

# Check for missing values
print("\nMissing values:")
print(weather_df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:")
print(weather_df.duplicated().sum())


# ============================================
# 3. LOAD
# ============================================

# Save the transformed data as a CSV file
weather_df.to_csv("processed_weather_data.csv", index=False)

print("\nProcessed weather data saved successfully.")

# Display the final dataset
print("\nFinal Dataset:")
print(weather_df)

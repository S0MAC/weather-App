import tkinter as tk
from tkinter import messagebox
import requests

# ----------------- Configuration -----------------
API_KEY = "your_openweathermap_api_key"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ----------------- Weather Fetch Function -----------------
def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

# ----------------- GUI Logic -----------------
def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Required", "Please enter a city name.")
        return

    data = get_weather_data(city)
    if data:
        try:
            temp = data['main']['temp']
            weather = data['weather'][0]['description'].title()
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            result_label.config(
                text=f"Weather in {city.title()}:\n"
                     f"Temperature: {temp}°C\n"
                     f"Condition: {weather}\n"
                     f"Humidity: {humidity}%\n"
                     f"Wind Speed: {wind_speed} m/s"
            )
        except (KeyError, TypeError):
            messagebox.showerror("Error", "Unexpected data format from API.")
    else:
        messagebox.showerror("Error", "City not found or API issue.")

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")
root.resizable(False, False)

city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=15)

search_button = tk.Button(root, text="Get Weather", command=show_weather, font=("Arial", 11))
search_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()

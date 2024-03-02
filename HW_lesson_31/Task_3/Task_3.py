#Task 3
"""
The Weather app
Write a console application which takes as an input a city name and returns current weather in the format of your choice.
For the current task, you can choose any weather API or website or use openweathermap.org 
"""

import requests
import tkinter as tk
from tkinter import messagebox, Label, Entry, Button

#colors
color_0 = '#ffffff'
color_1 = '#48484A'
color_2 = '#f55630'
color_3 = '#ffede9'

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry('350x200')
root.configure(background=color_0)
root.resizable(width=False, height=False)

# Frames
frame_up = tk.Frame(root, width= 350, height=50, bg=color_1)
frame_up.place(x=0, y=0)

frame_down = tk.Frame(root, width= 350, height=50, bg=color_0)
frame_down.place(x=0, y=50)

frame_info = tk.Frame(root, width=350, height=100, bg=color_3)
frame_info.place(x=0, y=110)

#frame_up
app_name = Label(frame_up, text="Погода", font=('Verdana 17 bold'), bg=color_1, fg=color_0)
app_name.place(x=10, y=10)

#frame_down
label_city = tk.Label(frame_down, text="Введіть місто", width=50, height=1, font=('Ivy 11'), bg=color_0, anchor=tk.NW)
label_city.place(x=10, y=18)
e_city = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
e_city.place(x=109, y=20)

# Define the function to fetch weather data
def fetch_weather():
    city = e_city.get()
    
    #API key
    api_key = "7a7c4003105d77f595e3c817075ded59"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"] - 273.15
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature:.0f}°C\nWeather: {weather}")
    except Exception as e:
            messagebox.showerror("Error", "Unable to fetch weather data")

# Create a button 
fetch_button = tk.Button(frame_down, text="Знайти", height=1, width=12, font=('Ivy 9 bold'), bg=color_2, fg=color_0, highlightthickness=0, command=fetch_weather)
fetch_button.place(x=245, y=17)


# Create a label to display weather information
weather_label = tk.Label(frame_info, text=" ", width=50, height=1, font=('Ivy 11'), bg=color_3, anchor=tk.NW)
weather_label.place(x=10, y=17)




root.mainloop()


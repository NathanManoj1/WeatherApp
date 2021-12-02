import requests
import tkinter as tk
from geopy.geocoders import Nominatim
import time
from datetime import datetime
def getWeather(canvas):
    geolocator = Nominatim(user_agent="my_user_agent")
    city =textField.get()
    loc = geolocator.geocode(city)
    api="https://api.weatherbit.io/v2.0/current?lat="+str(loc.latitude)+"&lon="+str(loc.longitude)+"&key=717e0079000445d991d6f8388675bbf6&include=minutely"
    json_data=requests.get(api).json()
    condition=json_data['data'][0]['weather']['description']
    temp = int(json_data['data'][0]['temp']) #Celsius
    print(temp)
    Atmosphericpressure=json_data['data'][0]['pres']
    print(Atmosphericpressure)
    #humidity=
    windspeed=json_data['data'][0]['wind_spd']
    
    sunset24 = time.strptime(json_data['data'][0]['sunset'],"%H:%M")
    sunrise24 = time.strptime(json_data['data'][0]['sunrise'],"%H:%M")
    sunrise12=time.strftime("%I:%M %p",sunrise24)
    sunset12=time.strftime("%I:%M %p",sunset24)
    print(condition)
    print(sunrise12)
    print(sunset12)
    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "Atmosphericpressure: " + str(Atmosphericpressure) +  "\n" +"Wind Speed: " + str(windspeed) + "\n" + "Sunrise: " + sunrise12 + "\n" + "Sunset: " + sunset12
    label1.config(text = final_info)
    label2.config(text = final_data) 
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
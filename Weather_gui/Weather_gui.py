from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter.ttk
import requests
import datetime

root = Tk()
root.geometry("900x600")
root.title("")
root.config(bg="#00C0D1")

#api-info
web_url="http://api.openweathermap.org/data/2.5/weather?"
key="3015a391e80a39e66e7a4f33692bdc6c"

def change_icon(val):
    if val == "01d":
        logov = Image.open("Clear_sky.png")
    elif val == "02d":
        logov = Image.open("few_clouds.png")
    elif val == "03d" or val == "03n":
        logov = Image.open("scattered clouds.png")
    elif val == "04d" or val == "04n":
        logov = Image.open("broken clouds.png")
    elif  val == "09d" or val == "09n":
        logov = Image.open("shower rain.png")
    elif val == "10d":
        logov = Image.open("rain.png")
    elif val == "11d" or val == "11n":
        logov = Image.open("thunderstorm.png")
    elif val == "13d" or val == "13n":
        logov = Image.open("snow.png")
    elif val == "50d" or val == "50n":
        logov = Image.open("mist.png")
    elif val == "01n":
        logov = Image.open("Clear_sky_night.png")
    elif val == "02n":
        logov = Image.open("few_clouds_night.png")
    elif val == "10n":
        logov = Image.open("rain_night.png")
    else:
        logov = Image.open("Clear_sky.png")
    resize_logo = logov.resize((300,300))
    weather_logo = ImageTk.PhotoImage(resize_logo)
    weather_logo_holder.config(image=weather_logo)
    weather_logo_holder.image=weather_logo

#hover
def hover_effect(source,hover_in,hover_out):
    source.bind("<Enter>", func=lambda e: source.config(bg=hover_in))
    source.bind("<Leave>", func=lambda e: source.config(source.config(bg=hover_out)))
def display(e):
    source = search_value.get()
    if source!="" and (source.isdigit() == False):
        url = web_url + "appid=" + key + "&q=" + source
        weather_data = requests.get(url)

        if weather_data.status_code==200:

            # changing the values of label as per the API data\

            change_icon(weather_data.json()['weather'][0]['icon'])
            city_name.config(text=weather_data.json()['name'])
            description.config(text=weather_data.json()['weather'][0]['description'])
            temprature.config(text=str(weather_data.json()['main']['temp'])+"°k | "+str(round(weather_data.json()['main']['temp']-273.15))+"°C")
            pressurer.config(text="Pressure :- "+str(weather_data.json()['main']['pressure'])+"hpa")
            humidity.config(text="Humidity :- "+str(weather_data.json()['main']['humidity'])+"%")
            wind_speed.config(text="Wind Speed :- "+str(weather_data.json()['wind']['speed'])+"m/s")

            current_time = datetime.datetime.now()
            time_zone.config(text=str(current_time))
        else:
            messagebox.showerror(title="error", message="Error city not found!")
    else:
        messagebox.showerror(title="error",message="Invalid! input")

# logo
Label(root,text="WEATHER FORECAST",font='arial 40',bg="#00A1DB").pack(side=TOP,fill=X)

search_value = StringVar()
search_input = Entry(root,textvariable=search_value,font="arial 20 italic",width=30)
search_input.place(x=115,y=100)

search_button = Button(root,text="SEARCH",bg="#95EE88",font="arial 20 bold",activebackground="#95EE88")
search_button.place(x=570,y=90)
hover_effect(search_button,"green","#95EE88")
search_button.bind("<Button-1>",display)

separator = tkinter.ttk.Separator(root,orient="horizontal")
separator.place(width=900,y=160,x=0)

#output layout
logo = Image.open("shower rain.png")
resize_logo = logo.resize((300,300))
weather_logo = ImageTk.PhotoImage(resize_logo)
weather_logo_holder = Label(image=weather_logo,bg="#00C0D1")
weather_logo_holder.place(x=120,y=162)

city_name = Label(root,text="demo",font='arial 30 bold',bg="#00C0D1")
city_name.place(x=220,y=170)

description = Label(root,text="rain fall",font='arial 20',bg="#00C0D1")
description.place(x=220,y=470)

temprature = Label(root,text="300°k | 27°C",font='arial 20',bg="#00C0D1")
temprature.place(x=180,y=430)

pressurer = Label(root,text="Pressure :- 1015hpa",font='arial 20',bg="#00C0D1")
pressurer.place(x=530,y=190)

humidity = Label(root,text="Humidity :- 64%",font='arial 20',bg="#00C0D1")
humidity.place(x=530,y=290)

wind_speed = Label(root,text="Wind Speed :- 0.62m/s",font='arial 20',bg="#00C0D1")
wind_speed.place(x=530,y=390)

searchtime=Label(root, text="--Time of Search--", font='arial 20', bg="#00C0D1")
searchtime.place(x=590, y=450)

time_zone = Label(root,text="dd-mm-yyyy hh:mm:ss.ssss",font='arial 20',bg="#00C0D1")
time_zone.place(x=530,y=490)

# seperators
separator = tkinter.ttk.Separator(root,orient="vertical")
separator.place(height=280,x=520,y=160)

separator = tkinter.ttk.Separator(root,orient="horizontal")
separator.place(width=900,x=520,y=240)

separator = tkinter.ttk.Separator(root,orient="horizontal")
separator.place(width=900,x=520,y=340)

separator = tkinter.ttk.Separator(root,orient="horizontal")
separator.place(width=900,x=520,y=440)

root.mainloop()

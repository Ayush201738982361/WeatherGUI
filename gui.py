import tkinter as tk
from tkinter import *
from tkinter import Image
from PIL import Image, ImageTk
from PIL import *
import requests
from requests import *


HEIGHT=800
WIDTH=900

root=tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()


frame=tk.Frame(root,bg='black')
frame.place(relx=0.1,rely=0.05,relheight=0.8,relwidth=0.8)


background_image=tk.PhotoImage(file="C:\\Users\\AYUSH\\OneDrive\\Desktop\\Screenshot (19).png")
label=tk.Label(frame,image=background_image)
label.place(relheight=1,relwidth=1)


lower_frame=tk.Frame(frame,bg='white')
lower_frame.place(relx=0.5,rely=0.2,relheight=0.7, relwidth=0.6,anchor='n')


entry=tk.Entry(frame,bd=8,background='#80c1ff',font=25,text='Gill Sans Ultra Bold')
entry.place(x=170,y=40,relheight=0.09,relwidth=0.7)


button=tk.Button(frame,text="Get Weather",bg='#80c1ff',fg='black',font=('Lucida Handwriting',13),bd=10,command=lambda:get_weather(entry.get()))
button.place(x=0,y=40)

label=tk.Label(lower_frame,font=('Gill Sans Ultra Bold',15))
label.place(relheight=1,relwidth=1)


def format_response(weather):
    try:
        name = weather['city']['name']
        desc = weather['list'][0]['weather'][0]['description']
        temp = weather['list'][0]['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s°C' % (name, desc, temp)
        return final_str

    except:
        return "No Such City"

def get_weather(city):
    weather_key='84f6a7e643d71887c2ecc2ccdf2fa11c'
    url='https://api.openweathermap.org/data/2.5/forecast'
    params={'APPID':weather_key,'q':city,'units':'metric'}
    response=requests.get(url,params=params)
    weather=response.json()

    city_name = weather['city']['name']
    temp = weather['list'][0]['main']['temp']
    weather_condition = weather['list'][0]['weather'][0]['description']

    formatted_weather = format_response(weather)
    if formatted_weather == "No Such City":
        label['text'] = formatted_weather
    else:
        print(f"City: {city_name}")
        print(f"Temperature: {temp}°F")
        print(f"Weather: {weather_condition}")
        label['text']=formatted_weather


root.mainloop()






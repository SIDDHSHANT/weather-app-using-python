from tkinter import *
from tkinter import ttk
import requests
def get_data():
    city = city_name.get()
    API_KEY = "a2fe38c0e7a815c0bed44d08d5d16675"  
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json()
    w_label_1.config(text = data["weather"][0]["main"])
    wd_label_1.config(text = data["weather"][0]["description"])
    temp_label_1.config(text = str(round(data["main"]["temp"] - 273.15, 2)) + "°C")
    temp_min_label_1.config(text = str(round(data["main"]["temp_min"] - 273.15, 2)) + "°C")
    temp_max_label_1.config(text = str(round(data["main"]["temp_max"] - 273.15, 2)) + "°C")
    pressure_label_1.config(text = str(data["main"]["pressure"]) + " hPa")


win = Tk()
win.title("Weather forecast")
win.config(bg =  "cyan")
win.geometry("500x500")
name_label = Label(win, text = "WEATHER FORECAST", font = ("Times New Roman", 20 , "bold"), 
bg = "SKYBLUE", fg = "black" , )
name_label.pack(pady=20)
name_label.place(x = 25, y = 40 , width = 450 , height = 50)
cities_states = [
    "Agra", "Uttar Pradesh",
    "Ahmedabad", "Gujarat",
    "Alwar", "Rajasthan",
    "Amla", "Madhya Pradesh",
    "Amritsar", "Punjab",
    "Aurangabad", "Maharashtra",
    "Bambora", "Rajasthan",
    "Bandhavgarh", "Madhya Pradesh",
    "Bangalore", "Karnataka",
    "Bharatpur", "Rajasthan",
    "Bhopal", "Madhya Pradesh",
    "Bhubaneshwar", "Orissa",
    "Bikaner", "Rajasthan",
    "Calicut", "Kerala",
    "Chail", "Himachal Pradesh",
    "Chamba", "Himachal Pradesh",
    "Chandigarh", "Punjab",
    "Chennai", "Tamil Nadu",
    "Chittorgarh", "Rajasthan",
    "Dalhousie", "Himachal Pradesh",
    "Darjeeling", "West Bengal",
    "Dausa", "Rajasthan",
    "Dehradun", "Uttar Pradesh",
    "Dharamshala", "Himachal Pradesh",
    "Durgapur", "West Bengal",
    "Gangtok", "Sikkim",
    "Goa", "Goa",
    "Gurgaon", "Haryana",
    "Hansi", "Haryana",
    "Haridwar", "Uttar Pradesh",
    "Hyderabad", "Andhra Pradesh",
    "Indore", "Madhya Pradesh",
    "Jaipur", "Rajasthan",
    "Jaisalmer", "Rajasthan",
    "Jalandhar", "Punjab",
    "Jamshedpur", "Jharkhand",
    "Jodhpur", "Rajasthan",
    "Kanha", "Madhya Pradesh",
    "Khimsar", "Rajasthan",
    "Kochin", "Kerala",
    "Kolkata", "West Bengal",
    "Kota", "Rajasthan",
    "Leh", "Jammu & Kashmir",
    "Lucknow", "Uttar Pradesh",
    "Ludhiana", "Punjab",
    "Madurai", "Tamil Nadu",
    "Mahabaleshwar", "Maharashtra",
    "Manali", "Himachal Pradesh",
    "Mandavi", "Gujarat",
    "Marchula", "Uttranchal",
    "Mathura", "Uttar Pradesh",
    "Mount Abu", "Rajasthan",
    "Mumbai", "Maharashtra",
    "Mussoorie", "Uttranchal",
    "Mysore", "Karnataka",
    "Nagaur Fort", "Rajasthan",
    "Nagpur", "Maharashtra",
    "Nainital", "Uttar Pradesh",
    "New Delhi", "Delhi",
    "Ooty", "Tamil Nadu",
    "Palampur", "Himachal Pradesh",
    "Pali", "Rajasthan",
    "Panchkula", "Haryana",
    "Pench", "Maharashtra",
    "Phalodi", "Rajasthan",
    "Port Blair", "Andaman & Nicobar Islands",
    "Pragpur", "Himachal Pradesh",
    "Pune", "Maharashtra",
    "Pushkar", "Rajasthan",
    "Ram Nagar", "Uttar Pradesh",
    "Ramgarh", "Rajasthan",
    "Ranakpur", "Rajasthan",
    "Ranthambore", "Rajasthan",
    "Rishikesh", "Uttar Pradesh",
    "Rohetgarh", "Rajasthan",
    "Sasan Gir", "Gujarat",
    "Sawai Madhopur", "Rajasthan",
    "Shimla", "Himachal Pradesh",
    "Shirdi", "Maharashtra",
    "Siana", "Rajasthan",
    "Srinagar", "Jammu & Kashmir",
    "Surat", "Gujarat",
    "Thekkady", "Kerala",
    "Thiruvananthapuram", "Kerala",
    "Tirupati", "Andhra Pradesh",
    "Udaipur", "Rajasthan",
    "Vapi", "Daman & Diu",
    "Vishakapatnam", "Andhra Pradesh"
]
city_name = StringVar()
com = ttk.Combobox(win, width = 27 , font = ("Times New Roman", 15 , "bold") , values = cities_states , textvariable = city_name)
com.place(x = 25, y = 100, width = 450, height = 30 )
com.set("Select a city")
w_label = Label(win, text = "Weather climate", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
w_label.place(x = 40, y = 240, width = 200, height = 30)
w_label_1 = Label(win, text = "", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
w_label_1.place(x = 280, y = 240, width = 200, height = 30)



wd_label = Label(win, text = "Weather description", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
wd_label.place(x = 40, y = 280, width = 200, height = 30)
wd_label_1 = Label(win, text = "", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
wd_label_1.place(x = 280, y = 280, width = 200, height = 30)

temp_label = Label(win, text = "Temperature", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
temp_label.place(x = 40, y = 320, width = 200, height = 30)
temp_label_1 = Label(win, text = "", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
temp_label_1.place(x = 280, y = 320, width = 200, height = 30)

temp_min_label = Label(win, text = "Minimum temperature", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
temp_min_label.place(x = 40, y = 360, width = 200, height = 30)
temp_min_label_1 = Label(win, text = "", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
temp_min_label_1.place(x = 280, y = 360, width = 200, height = 30)

temp_max_label = Label(win, text = "Maximum temperature", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
temp_max_label.place(x = 40, y = 400, width = 200, height = 30)
temp_max_label_1 = Label(win, text = " ", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
temp_max_label_1.place(x = 280, y = 400, width = 200, height = 30)

pressure_label = Label(win, text = "Pressure", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
pressure_label.place(x = 40, y = 440, width = 200, height = 30)
pressure_label_1 = Label(win, text = "", font = ("Times New Roman", 15 ), bg = "lightyellow", fg = "black")
pressure_label_1.place(x = 280, y = 440, width = 200, height = 30)

done_button = Button(win, text = "Done", font = ("Times New Roman", 15 , "bold"), bg = "SKYBLUE", fg = "black" , command = get_data)
done_button.place(x = 25, y = 160, width = 450, height = 30)

win.mainloop()
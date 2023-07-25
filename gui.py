import tkinter as tk
from tkinter import messagebox
from API_Manager import API_Manager

window = tk.Tk()
window.geometry("500x200")
def display_weather():
    city = user_input.get()
    output = API_Manager.get_current_weather(city)
    output_label.config(text=output)


greeting = tk.Label(text="Please enter your city: ", font=('Arial', 15))
greeting.pack()
user_input = tk.StringVar(window)
entry = tk.Entry(window, textvariable=user_input)
entry.pack()
button = tk.Button(
    text="Get current weather!",
    width=20,
    height=2,
    bg="blue",
    fg="yellow",
    command = display_weather
)
button.pack()

output_label = tk.Label(text="", font=('Arial', 25))
output_label.pack()

window.mainloop()
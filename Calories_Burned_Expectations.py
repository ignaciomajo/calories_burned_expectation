"""
This app implements the model trained in the 'Calories_Burned_Analysis', allowing user to complete the required inputs to predict how many calories can that person
expect to burn in one workout session and in a whole month (30 days)

REQUIREMENTS

Pandas, Numpy, Sklearn

"""

#################### LIBRARIES IMPORT SECTION #################### 

import numpy as np
import pandas as pd
import math
import sklearn
import joblib
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


#################### VARIABLES AND FUNCTIONS SECTION ####################


columns = ['Age', 'Avg_BPM', 'Session_Duration (hours)', 'Water_Intake (liters)', 
           'Weight_log', 'HIIT', 'Strength', 'Yoga', 'Gender_Mapped']
to_predict = []
scaler = joblib.load("C:\\Users\\Ignacio\\JupyterScripts\\Kaggle\\Calories_Burned_Project\\models\\scaler_calories.joblib")
model = joblib.load("C:\\Users\\Ignacio\\JupyterScripts\\Kaggle\\Calories_Burned_Project\\models\\model_calories.joblib")

    
def calculate():
    """
    This function will get all values from Entries and Comboboxes, and then prepare the data to scale and to feed the model for making predictions
    The result is the expected amount of calories burned in a single workout session
    """

    # Age

    age = age_box.get()
    if not age:
        messagebox.showerror(title='Error', message='Please complete all (*) fields')
    elif not age.isdecimal():
        messagebox.showerror(title='Error', message='"Age" field must be a number')
    else:
        age = float(age)

    #Gender

    gender = gender_box.get()
    if not gender:
        messagebox.showerror(title='Error', message='Please complete all (*) fields')
    elif gender == 'Male':
        gender = 0
    else:
        gender = 1

    # Avg_BPM

    avg_bpm = avg_bpm_box.get()
    if not avg_bpm:
        avg_bpm = 143.76
    try:
        avg_bpm = float(avg_bpm)
    except ValueError:
        messagebox.showerror(title='Error', message='"Avg BPM" field must be a number')
    
    # Session Duration

    session_duration = session_duration_box.get()
    try:
       session_duration = float(session_duration)
    except ValueError:
        messagebox.showerror(title='Error', message='"Session Duration" field must be a number')
    except Exception:
        messagebox.showerror(title='Error', message='Please complete all (*) fields')
    

    # Water Intake

    water_intake = water_intake_box.get()
    if not water_intake:
        messagebox.showerror(title='Error', message='Please complete all (*) fields')
    else:
        try:
            water_intake = float(water_intake)
        except ValueError:
            messagebox.showerror(title='Error', message='"Water Intake (liters)" field must be a number')

    # Workout Frequency

    workout_freq = workout_freq_box.get()
    if not workout_freq:
        messagebox.showerror(title='Error', message='Please complete all (*) fields')
    else:
        workout_freq = int(workout_freq)
    
    # Weight Log

    weight_log = weight_box.get()
    try:
        weight_log = float(weight_log)
        weight_log = math.log(weight_log)
    except ValueError:
        messagebox.showerror(title='Error', message='"Weight (kg)" field must be a number')
    except Exception:
        messagebox.showerror(title='Error', message='Please complete all (*) fields')


    # Workout Type

    workout_type = workout_type_box.get()
    if not workout_type:
        messagebox.showerror(title='Error', message='Please complete all (*) fields')
    elif workout_type == 'Cardio':
        workout_type = [0, 0, 0]
    elif workout_type == 'HIIT':
        workout_type = [1, 0, 0]
    elif workout_type == 'Strength':
        workout_type = [0, 1, 0]
    else:
        workout_type = [0, 0, 1]

    # Prepare data for predictions

    global to_predict

    to_predict = [age, avg_bpm, session_duration, water_intake, weight_log]
    for i in workout_type:
        to_predict.append(i)

    to_predict.append(gender)

    to_predict = np.array(to_predict).reshape(-1, 1)
    to_predict = scaler.fit_transform(to_predict)
    to_predict = pd.DataFrame(to_predict.T, columns=columns)

    # Predictions 

    calories = model.predict(to_predict)
    calories_month = calories * np.floor(((30 / 7) * workout_freq))

    # Show results
    
    calories_label.config(text=np.round(calories, 2), font=(None, 16, 'bold'))
    calories_month_label.config(text=np.round(calories_month, 2), font=(None, 16, 'bold'))


def clean():
    """
    This function will clean all fields in the app
    """
    age_box.delete(0, tk.END)
    session_duration_box.delete(0, tk.END)
    weight_box.delete(0, tk.END)
    avg_bpm_box.delete(0, tk.END)
    water_intake_box.delete(0, tk.END)
    
    gender_box.set("")
    workout_freq_box.set("")
    workout_type_box.set("")

    calories_label.config(text="")
    calories_month_label.config(text="")

    
#################### GRAPHIC SECTION ####################


window = tk.Tk()

window.title('Calories Burned Expectation')
window.config(width=460, height=430, bg='Slategray2')
window.resizable(False, False)

logo = tk.PhotoImage(file=r'C:\\Users\\Ignacio\\JupyterScripts\\Kaggle\\Calories_Burned_Project\\icon4.png')
window.iconphoto(True, logo)


# Header label

header_label = tk.Label(text='Calculate the calories burned during your workout', bg='Slategray2', font=(None, 12, 'bold', 'italic'))
header_label.place(x=20, y=10)

# Age field

age_label = tk.Label(text='Age (*)', bg='Slategray2')
age_label.place(x=20, y=50)
age_box = tk.Entry(justify='left')
age_box.place(x=20, y=70)

# Session_Duration field

session_duration_label = tk.Label(text='Session Duration (hours) (*)', bg='Slategray2')
session_duration_label.place(x=20, y=100)
session_duration_box = tk.Entry(justify='left')
session_duration_box.place(x=20, y=120)

# Weight_log field

weight_label = tk.Label(text='Weight (kg) (*)', bg='Slategray2')
weight_label.place(x=20, y=150)
weight_box = tk.Entry(justify='left')
weight_box.place(x=20, y=170)


# Water_Intake field

water_intake_label = tk.Label(text='Water Intake (liters) (*)', bg='Slategray2')
water_intake_label.place(x=20, y=200)
water_intake_box = tk.Entry(justify='left')
water_intake_box.place(x=20, y=220)

# Gender field

gender_label = tk.Label(text='Gender (*)', bg='Slategray2')
gender_label.place(x=220, y=50)
gender_box = ttk.Combobox(
                    state='readonly',
                    values=['Male', 'Female']
                    )
gender_box.place(x=220, y=70)

# Workout_Frequency (days/week) field

workout_freq_label = tk.Label(text='Workout Frequency (days/week) (*)', bg='Slategray2')
workout_freq_label.place(x=220, y=100)
workout_freq_box = ttk.Combobox(
                            state='readonly',
                            values=[1, 2, 3, 4, 5, 6, 7]
)
workout_freq_box.place(x=220, y=120)

#Workout_Type field

workout_type_label = tk.Label(text='Workout Type (*)', bg='Slategray2')
workout_type_label.place(x=220, y=150)
workout_type_box = ttk.Combobox(
                            state='readonly',
                            values=['Cardio','HIIT', 'Strenght','Yoga']
)
workout_type_box.place(x=220, y=170)

#Avg_BPM field

avg_bpm_label = tk.Label(text='Avg BPM', bg='Slategray2')
avg_bpm_label.place(x=220, y=200)
avg_bpm_box = tk.Entry(justify='left')
avg_bpm_box.place(x=220, y=220)

# Buttons

calculate_button = tk.Button(text='Calculate Calories Burned', command=calculate)
calculate_button.place(x=20, y=270)

clear_button = tk.Button(text='Reset', command=clean)
clear_button.place(x=20, y=320)

expectation_label = tk.Label(text='Expected Burned Calories in one session:', bg='Slategray2')
expectation_label.place(x=220, y=260)

calories_label = tk.Label(text='', bg='Slategray2')
calories_label.place(x=220, y=280)

expectation_month_label = tk.Label(text='Expected Burned Calories in one month:', bg='Slategray2')
expectation_month_label.place(x=220, y=320)

calories_month_label = tk.Label(text='', bg='Slategray2')
calories_month_label.place(x=220, y=340)

window.mainloop()
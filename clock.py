# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 10:14:31 2025

@author: Hemal
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to draw a clock with given hour and minute
def draw_clock(hour, minute):
    fig, ax = plt.subplots()
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw clock face
    circle = plt.Circle((0, 0), 1, color='white', edgecolor='black', fill=False, linewidth=2)
    ax.add_artist(circle)

    # Draw hour numbers
    for i in range(12):
        angle = np.pi/2 - i * np.pi/6
        x = np.cos(angle)
        y = np.sin(angle)
        ax.text(x * 0.85, y * 0.85, str(i if i != 0 else 12), ha='center', va='center', fontsize=12)

    # Draw hour hand
    hour_angle = np.pi/2 - (hour % 12 + minute/60) * np.pi/6
    hour_x = np.cos(hour_angle) * 0.6
    hour_y = np.sin(hour_angle) * 0.6
    ax.plot([0, hour_x], [0, hour_y], color='black', linewidth=6)

    # Draw minute hand
    minute_angle = np.pi/2 - minute * np.pi/30
    minute_x = np.cos(minute_angle) * 0.8
    minute_y = np.sin(minute_angle) * 0.8
    ax.plot([0, minute_x], [0, minute_y], color='black', linewidth=4)

    return fig

# Function to convert time to a descriptive sentence
def time_to_sentence(hour, minute):
    display_hour = hour % 12
    if display_hour == 0:
        display_hour = 12

    if minute == 0:
        return f"It is {display_hour} o'clock."
    elif minute == 15:
        return f"It is quarter past {display_hour}."
    elif minute == 30:
        return f"It is half past {display_hour}."
    elif minute == 45:
        return f"It is quarter to {(display_hour % 12) + 1}."
    elif minute < 30:
        return f"It is {minute} minutes past {display_hour}."
    else:
        return f"It is {60 - minute} minutes to {(display_hour % 12) + 1}."

# Streamlit UI
st.title("Learn to Tell Time")

st.write("Welcome to the time-telling learning tool! Adjust the sliders to see the time on the clock.")

# Inputs
hour = st.slider("Hour", 0, 23, 12)
minute = st.slider("Minute", 0, 59, 0)

# Display the clock
clock_fig = draw_clock(hour, minute)
st.pyplot(clock_fig)

# Explanation
time_sentence = time_to_sentence(hour, minute)
st.write(time_sentence)

# Additional explanation for children
st.write("""
### How to Read the Time:
1. **Hour Hand**: The short hand points to the hour. If it's between two numbers, it means the time is part of the next hour.
2. **Minute Hand**: The long hand points to the minutes. Each number on the clock represents 5 minutes.
3. **Reading the Time**:
   - Look at the hour hand first. If it's exactly on a number, that's the hour.
   - If the hour hand is between numbers, it means we're partway through that hour.
   - Look at the minute hand. If it's on a number, multiply that number by 5 to get the minutes.
   - If the minute hand is between numbers, estimate how many minutes past the hour it is.

### Special Time Phrases:
- **Half Past**: When the minute hand is on the 6, it's "half past" the hour. For example, 3:30 is "half past three."
- **Quarter Past**: When the minute hand is on the 3, it's "quarter past" the hour. For example, 3:15 is "quarter past three."
- **Quarter To**: When the minute hand is on the 9, it's "quarter to" the next hour. For example, 3:45 is "quarter to four."
""")

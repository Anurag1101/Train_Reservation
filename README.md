# Train Reservation System

## Overview
This Python-based Train Reservation System allows users to simulate booking train tickets. The program asks for passenger details, such as name, age, gender, source and destination stations, and coach type (AC, Sleeper, or Unreserved). It then provides a confirmed berth, coach number, and calculates the fare based on the coach type.

## Features
- Simulates ticket booking with user inputs.
- Provides random berth and coach number assignments.
- Calculates fare based on the type of coach (AC, Sleeper, or Unreserved).
- Includes a greeting message from Indian Railways.
- Static methods to display welcome and farewell messages.

## How to Use
**Clone the repository**:
git clone https://github.com/Anurag1101/Train_Reservation.git

Navigate to the project directory:
cd Train_Reservation

**Run the program:** Run the Python script in your terminal or Python environment:
python train_reservation.py

**User Inputs:** The program will prompt you to enter the following information:

    Train Number
    Passenger Name
    Passenger Age
    Passenger Gender (M/F)
    Source Station
    Destination Station
    Coach Type (AC, SL, Unreserved)**

**Example Output:**

  Welcome to Indian Railways
  Ticket booked for Anurag 25M in Train no 1101 from Mumbai to Delhi.
  Your berth no is 42 and Coach no is A3.
  The fare of your journey is ₹1500.
  Indian Railway wishes you a Happy and Safe journey.

**Code Structure**:

    **Train Class** : This class represents a train ticket booking system.
    __init__: Initializes passenger details (train number, name, age, gender, etc.).
    **book()**: Books a ticket for the passenger.
    **berth_and_fare()**: Assigns a random berth, coach number, and calculates the fare.
    **greet() & greet1()**: Static methods to display welcome and farewell messages.

**Future Enhancements**:
Implement an actual fare calculator based on distance.
Add more details such as seat preferences (Window, Middle, Aisle).
Include error handling for invalid inputs.
Improve the user interface with a graphical or web-based version.

**Requirements:**
Python 3.x
random module (standard library)

**License**:
This project is licensed under the MIT License. See the LICENSE file for details.

**Author**:
**Anurag Tiwari**

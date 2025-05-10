# OOP Lab Project

This repository contains an Object-Oriented Programming (OOP) project implemented in Python, created as part of an ITI lab assignment. The project simulates a system with `Person`, `Car`, `Employee`, and `Office` classes, focusing on an employee's daily routine, including driving to work and managing office interactions. The implementation follows the lab requirements from pages 5–11, with a custom fuel consumption model (1 unit per km) and a lateness check based on a driving velocity of 60 km/h.

## Project Overview

The project models an employee (e.g., Khaled) who:
- Performs daily activities (sleeping, eating, buying items).
- Drives a car to the ITI Smart Village office (20 km away).
- Is managed by an office that checks if they arrive before 9:00 AM, rewarding or deducting salary accordingly.

## Features

- **Person Class**: Manages attributes like `name`, `money`, `mood`, and `healthRate`, with methods:
  - `sleep(hours)`: Sets `mood` to "happy" (7 hours), "tired" (<7), or "lazy" (>7).
  - `eat(meals)`: Sets `healthRate` to 100% (3 meals), 75% (2), or 50% (1).
  - `buy(items)`: Decreases `money` by 10 LE per item.
- **Car Class**: Handles vehicle operations with `fuelRate` (0–100) and `velocity` (0–200), including:
  - `run(velocity, distance)`: Simulates driving, consuming 1 unit of fuel per km, and stores `driving_velocity`.
  - `stop(remaining_distance)`: Stops the car and sets `velocity` to 0.
- **Employee Class**: Extends `Person` with attributes like `id`, `car`, `email`, `salary`, and `distanceToWork`, with methods:
  - `work(hours)`: Sets `mood` to "happy" (8 hours), "tired" (>8), or "lazy" (<8).
  - `drive()`: Calls `car.run(60, distanceToWork)`.
  - `refuel(gasAmount)`: Adds `gasAmount` to `fuelRate`, capped at 100.
  - `send_mail()`: Prints an email message.
- **Office Class**: Manages employees with class attribute `employees_num` and methods:
  - `hire(employee)`, `fire(emp_id)`, `deduct(emp_id, deduction)`, `reward(emp_id, reward)`.
  - `check_lateness(emp_id, move_hour)`: Checks if the employee arrives before 9:00 AM using `driving_velocity`.
  - `calculate_lateness(target_hour, move_hour, distance, velocity)`: Computes arrival time.

## Prerequisites

- Python 3.x
- No external libraries required (uses standard Python).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/khaled0x01/Python-Projects.git

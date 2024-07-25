import googlemaps
from datetime import datetime, timedelta
import pandas as pd
from flask import Flask, render_template, jsonify
import json
from randomize_car_battery_levels import CarData
from station import Station, get_station_info
from charger import optimal_charging_rate
import random

app = Flask(__name__)

# Fetch set of 50 randomly generated EVs that need charging
car_data_manager = CarData('EV_Database_UK.csv', num_cars=50)
car_charging_battery_levels_data = car_data_manager.get_car_charging_battery_levels_data()

# Initialize an array that includes these 50 cars and their relevant variables, including the optimized charging speed simulated for each EV
vehicle_parameters = {}

# Update vehicle_parameters with new data
for index, car_info in enumerate(car_charging_battery_levels_data, start=1):
    car_name = f"electric_car_{index}"
    vehicle_parameters[car_name] = {
        'Vehicle Type': car_info['Car'],
        'Battery Capacity (kWh)': car_info['battery_capacity'],
        'Charging Speed (kW)': car_info['charging_speed'],
        'Optimal Charging Speed (kW)': optimal_charging_rate(car_info['charging_speed'], car_info['Car'], car_info['battery_level']),
        'Battery Level': car_info['battery_level'],
        'Max Duration': car_info['max_duration']
    }

# Fetch station information
stations = get_station_info()

# Calculate the required energy to reach the max battery level (80% for now)
def calculate_energy_requirement_opt(vehicle_params):
    battery_capacity = vehicle_params['Battery Capacity (kWh)']
    current_battery_level = vehicle_params['Battery Level']
    max_battery_level = 80
    required_energy_opt = (max_battery_level - (current_battery_level / 100)) * float(battery_capacity)
    return required_energy_opt

def calculate_energy_requirement_rdm(vehicle_params):
    battery_capacity = vehicle_params['Battery Capacity (kWh)']
    current_battery_level = vehicle_params['Battery Level']
    required_energy_rdm = (100 - (current_battery_level / 100)) * float(battery_capacity)
    return required_energy_rdm

def calculate_energy_losses(power, time_hours):
    resistance = 0.1  # Ohms
    losses = (power ** 2) * float(resistance) * float(time_hours)
    return losses

def allocate_charging_tasks(vehicle_parameters, stations):
    charging_plan = []

    # Iterate over each vehicle
    for index, vehicle in vehicle_parameters.items():
        vehicle_type = vehicle['Vehicle Type']
        current_battery_level = vehicle['Battery Level']
        max_duration = vehicle['Max Duration']
        optimal_charging_speed = vehicle['Optimal Charging Speed (kW)']
        battery_capacity = vehicle['Battery Capacity (kWh)']

        # Calculate the required energy for optimal charging speed of the vehicle
        required_energy_opt = calculate_energy_requirement_opt(vehicle)

        for station in stations:
            if float(station[4]) + float(optimal_charging_speed) <= float(station[3]):

                actual_charging_duration_hours = min(max_duration, required_energy_opt / float(optimal_charging_speed))
                energy_provided = actual_charging_duration_hours * float(optimal_charging_speed)
                final_battery_level = current_battery_level + (energy_provided / float(battery_capacity) * 100)
                final_battery_level = min(final_battery_level, 80)

                # Calculate energy losses
                losses = calculate_energy_losses(float(optimal_charging_speed), actual_charging_duration_hours)


                # Update the current load of the station
                station[4] += optimal_charging_speed

                # Append the charging plan for this vehicle
                charging_plan.append({
                    'vehicle_type': vehicle_type,
                    'station_id': station[0],
                    'current_battery_level': current_battery_level,
                    'max_duration': max_duration,
                    'energy_requirement': required_energy_opt,
                    'charging_rate': optimal_charging_speed,
                    'actual_charging_duration_hours': actual_charging_duration_hours,
                    'final_battery_level': final_battery_level,
                    'station_current_load': station[4],
                    'energy_losses': losses
                })

                # Move to the next vehicle once a suitable station is found
                break

    return charging_plan

def random_charging_tasks(vehicle_parameters, stations):
    random_plan = []

    for index, vehicle in vehicle_parameters.items():
        vehicle_type = vehicle['Vehicle Type']
        current_battery_level = vehicle['Battery Level']
        max_duration = vehicle['Max Duration']
        battery_capacity = vehicle['Battery Capacity (kWh)']
        required_energy_rdm = calculate_energy_requirement_rdm(vehicle)
        charging_speed = float(vehicle['Charging Speed (kW)'])

        # Randomly select a station
        station = random.choice(stations)

        if float(station[4]) + charging_speed <= float(station[3]):
            actual_charging_duration_hours = min(max_duration, required_energy_rdm / charging_speed)
            energy_provided = actual_charging_duration_hours * charging_speed
            final_battery_level = current_battery_level + (energy_provided / float(battery_capacity) * 100)
            final_battery_level = min(final_battery_level, 100)

            # Calculate energy losses
            losses = calculate_energy_losses(charging_speed, actual_charging_duration_hours)
            station[4] += charging_speed  # Update the actual load of the station


            random_plan.append({
                'vehicle_type': vehicle_type,
                'station_id': station[0],
                'current_battery_level': current_battery_level,
                'time_available_hours': max_duration,
                'energy_requirement_rdm': required_energy_rdm,
                'charging_rate': charging_speed,
                'actual_charging_duration_hours': actual_charging_duration_hours,
                'final_battery_level': final_battery_level,
                'station_current_load': station[4],
                'energy_losses': losses
            })

    # Debug: print the random plan length and details
    print(f"\nTotal number of vehicles in the random plan: {len(random_plan)}")
    for plan in random_plan:
        print(plan)

    return random_plan

# Example usage
optimized_charging_plan = allocate_charging_tasks(vehicle_parameters.copy(), stations.copy())
random_charging_plan = random_charging_tasks(vehicle_parameters.copy(), stations.copy())

# Calculate total energy losses for each plan
total_optimized_losses = sum(plan['energy_losses'] for plan in optimized_charging_plan)
total_random_losses = sum(plan['energy_losses'] for plan in random_charging_plan)

print(f"Total optimized energy losses: {total_optimized_losses:.2f} kWh")
print(f"Total random energy losses: {total_random_losses:.2f} kWh")

# Display the charging plan
print("\nOptimized Charging Plan:")
for plan in optimized_charging_plan:
    print(plan)

print("\nRandom Charging Plan:")
for plan in random_charging_plan:
    print(plan)

# Route to display the data
@app.route('/')
def index():
    return render_template('index.html',
                           optimized_charging_plan=optimized_charging_plan,
                           random_charging_plan=random_charging_plan,
                           total_optimized_losses=total_optimized_losses,
                           total_random_losses=total_random_losses)


if __name__ == '__main__':
    app.run(debug=True)

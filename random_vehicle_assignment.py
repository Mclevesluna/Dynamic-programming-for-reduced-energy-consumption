# This script simulates a charging station for electric vehicles. It allows users to select a vehicle type from a CSV file,
# input current charging level and maximum duration, and then displays the selected vehicle type along with the provided charging information.

import random
import csv

class ChargingStation:
    def __init__(self, station_name):
        self.station_name = station_name
        self.vehicle_types = []

    def load_vehicle_types_from_csv(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            # Skip the header row
            next(reader)
            for row in reader:
                vehicle_name = row[0]
                self.vehicle_types.append(vehicle_name)

    def select_vehicle_type(self):
        print("Available vehicle types:")
        for index, vehicle_type in enumerate(self.vehicle_types, start=1):
            print(f"{index}. {vehicle_type}")
        choice = input("Enter the number corresponding to the desired vehicle type: ")
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.vehicle_types):
                return self.vehicle_types[choice_index]
            else:
                print("Invalid choice. Please enter a valid number.")
                return self.select_vehicle_type()  # Recursively call select_vehicle_type until a valid choice is made
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.select_vehicle_type()

    def assign_random_charging_level(self):
        charging_levels = ["low", "medium", "high"]
        return random.choice(charging_levels)

    def get_current_charging(self):
        if self.current_charging:
            return f"{self.current_charging}%"
        return self.current_charging

    def set_current_charging(self):
      # Get user input for charging information
        charging_info = input("Enter current charging level :")
        self.current_charging = charging_info

    def set_max_duration(self):
        # Get user input for max duration
        duration_input = input("Enter maximum duration for charging in hours: ")
        try:
            self.max_duration = float(duration_input)
        except ValueError:
            print("Invalid input. Please enter a valid number for maximum duration.")
            self.set_max_duration()


# Test case example:
station = ChargingStation("Busy Chargers")
station.load_vehicle_types_from_csv("EV_Database_UK.csv")
selected_vehicle_type = station.select_vehicle_type()
print("Selected vehicle type:", selected_vehicle_type)

station.set_current_charging()

station.set_max_duration()

if station.get_current_charging():
    print("Current charging information:", station.get_current_charging())

# Print the final output
print(f"Selected Vehicle: {selected_vehicle_type}")
print(f"Charging Information: {station.get_current_charging()}")
print(f"Maximum Duration for Charging: {station.max_duration} hours")
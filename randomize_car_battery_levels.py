# # This script generates simulated data for electric cars' charging and battery levels. It reads car data from a CSV file, randomly selects a specified number of cars, and assigns random charging speeds,
# # battery levels, and other parameters to each car. The generated data can be used for analysis or simulations related to electric vehicles.

# import random
# import csv

# class CarData:
#     def __init__(self, csv_file, num_cars=185):
#         self.car_array = self.read_and_select_cars(csv_file, num_cars)
#         self.car_charging_battery_levels_data = self.assign_charging_and_battery_levels()

#     def randomize_battery_level(self):
#         return random.randint(0, 50)

#     def read_and_select_cars(self, csv_file, num_cars):
#         try:
#             with open(csv_file, 'r') as file:
#                 reader = csv.DictReader(file)
#                 car_array = [row for row in reader]
#         except FileNotFoundError:
#             print("The CSV file was not found.")
#             exit(1)

#         if len(car_array) < num_cars:
#             print("The CSV file does not contain enough cars.")
#             exit(1)

#         return random.sample(car_array, num_cars)

#     def assign_charging_and_battery_levels(self):
#         car_charging_battery = {}
#         for car in self.car_array:
#             charging_speed = float(car.get('Charging Speed (miles/min)', '0'))
#             max_duration = random.randint(1, 8)  # Random max duration in hours (assuming 1 to 8 hours)
#             battery_level = self.randomize_battery_level()
#             car_charging_battery[car['Cars']] = {
#                 'Car': car['Cars'],
#                 'battery_level': battery_level,
#                 'battery_capacity': car['Battery Capacity (kWh)'],
#                 'range': car['Range (miles)'],
#                 'charging_speed': charging_speed,
#                 'max_duration': float(max_duration)
#             }
#         return car_charging_battery

#     def get_car_charging_battery_levels_data(self):
#         return list(self.car_charging_battery_levels_data.values())

# # Example usage:
# car_data_manager = CarData('EV_Database_UK.csv', num_cars=185)
# car_charging_battery_levels_data = car_data_manager.get_car_charging_battery_levels_data()

# for index, car_info in enumerate(car_charging_battery_levels_data, start=1):
#     print(f"{index}. Vehicle Type: {car_info['Car']}: Battery Level: {car_info['battery_level']}%, Battery Capacity: {car_info['battery_capacity']} KWh, Range: {car_info['range']}, Max Duration: {car_info['max_duration']}, Charging Speed: {car_info['charging_speed']}")



import random
import csv

class CarData:
    def __init__(self, csv_file, num_cars=500):
        self.car_array = self.read_and_select_cars(csv_file, num_cars)
        self.car_charging_battery_levels_data = self.assign_charging_and_battery_levels()

    def randomize_battery_level(self):
        return random.randint(0, 50)

    def read_and_select_cars(self, csv_file, num_cars):
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                car_array = [row for row in reader]
        except FileNotFoundError:
            print("The CSV file was not found.")
            exit(1)

        while len(car_array) < num_cars:
            car_array += random.sample(car_array, min(num_cars - len(car_array), len(car_array)))

        return car_array

    def assign_charging_and_battery_levels(self):
        car_charging_battery = {}
        for car in self.car_array:
            charging_speed = float(car.get('Charging Speed (miles/min)', '0'))
            max_duration = random.randint(1, 8)  # Random max duration in hours (assuming 1 to 8 hours)
            battery_level = self.randomize_battery_level()
            car_charging_battery[car['Cars']] = {
                'Car': car['Cars'],
                'battery_level': battery_level,
                'battery_capacity': car['Battery Capacity (kWh)'],
                'range': car['Range (miles)'],
                'charging_speed': charging_speed,
                'max_duration': float(max_duration)
            }
        return car_charging_battery

    def get_car_charging_battery_levels_data(self):
        return list(self.car_charging_battery_levels_data.values())

# Example usage:
car_data_manager = CarData('EV_Database_UK.csv', num_cars=500)
car_charging_battery_levels_data = car_data_manager.get_car_charging_battery_levels_data()

for index, car_info in enumerate(car_charging_battery_levels_data, start=1):
    print(f"{index}. Vehicle Type: {car_info['Car']}: Battery Level: {car_info['battery_level']}%, Battery Capacity: {car_info['battery_capacity']} KWh, Range: {car_info['range']}, Max Duration: {car_info['max_duration']}, Charging Speed: {car_info['charging_speed']}")

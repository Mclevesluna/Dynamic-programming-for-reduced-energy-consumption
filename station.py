import googlemaps
import random
from geopy.distance import geodesic

class Station:
    def __init__(self, station_id, name, address, location, num_chargers, max_loads, current_load):
        self.station_id = station_id
        self.name = name
        self.num_chargers = num_chargers
        self.location = location
        self.address = address
        self.max_loads = max_loads
        self.current_load = current_load
        # self.sorting_index = sorting_index

    def __str__(self):
        # return f"{self.station_id} = Station Name: {self.name}, Number of Chargers: {self.num_chargers}, Location: {self.location}, Sorting Index: {self.sorting_index}"
        # return f"{self.station_id} = Station Name: {self.name}, Address: {self.address}, Location: {self.location} Number of Chargers: {self.num_chargers}"
        return f"Station Name: {self.name}, Address: {self.address}, Location: {self.location}, Number of Chargers: {self.num_chargers}, Max Loads: {self.max_loads}, Current Load: {self.current_load}"

def randomize_chargers():
        # Weights for the number of chargers from 2 to 14
        # Weights for 2-8 are higher to make their selection more likely
        numbers = list(range(2, 15))  # Numbers from 2 to 14
        weights = [10] * 7 + [1] * 6  # Weights: 10 for numbers 2-8, 1 for numbers 9-14
        return random.choices(numbers, weights=weights, k=1)[0]  # Return one number based on weights

# Randomize the loads for single station with the number of chargers
def randomize_loads(num_chargers):
    max_loads = []
    sum_loads = 0

# two randomisation choices for normal chargers: 43kW, 50kW, super charger power choices: 100kW, 150kW
    # Randomosation for specifying if the charging station is super or normal

    # To specify whether the charging station is for super charger or normal charger in algorithm.py
    # Simply divide the max_loads by number of chargers, if <= 50, then normal charging station, else a super charging station

    # 0 for super, 1 for normal
    super_normal = random.choices([0, 1], weights=[0.1, 0.9], k=1)
    if super_normal[0] == 0:
        for _ in range(num_chargers):
            max_loads.append(random.choices([100, 150], weights=[0.3, 0.7], k=1))
            sum_loads += max_loads[-1][0]
        
    else:

        # Randomize the loads for each station
        for _ in range(num_chargers):
            
            max_loads.append(random.choices([43, 50], weights=[0.3, 0.7], k=1))
            sum_loads += max_loads[-1][0]

    return sum_loads

# getter for station info
# station_data = {
#     'StationID': ['Station_1', 'Station_2', 'Station_3'],
#     'CurrentLoad': [0, 0, 0],  # initial load in kW
#     'MaxLoad': [100, 100, 100]  # example max load per station in kW
# }
def get_station_info():
    station_info = []
    for station in evc_stations:
        station_info.append([station.station_id, station.name, station.num_chargers, station.max_loads, station.current_load ,station.location, station.address])
    return station_info

@property
def station_info(self):
    return self.station_info

@station_info.setter
def station_info(self, station_info):
    self.station_info = station_info

gmaps = googlemaps.Client(key='AIzaSyBLjHdsR8lgPHUd4haJVIKPFgYnHvBsOF8')

temp_index = 0

# Check if geocoding was successful
while True:
    # Take user input for location
    user_location = input("Enter the location (or type 'exit' to quit): ")
    # Exit the loop if the user types 'exit'
    if user_location.lower() == 'exit':
        break

    try:
        # Geocode the user input
        geocode_result = gmaps.geocode(user_location)
        # Failed to geocode the location
        if not geocode_result:
            print("Please try again:")
            continue  # Skip the rest of the loop and prompt again

        # If geocoding was successful, proceed to search for EVC stations
        # Extract latitude and longitude from geocode result
        lat_lng = f"{geocode_result[0]['geometry']['location']['lat']},{geocode_result[0]['geometry']['location']['lng']}"

        # Search for EVC stations and sort them by distance from the user's location
        stations = gmaps.places_nearby(location=lat_lng, radius=1000, keyword='ev charging station nearby')
        stations['results'].sort(key=lambda x: geodesic((geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']), (x['geometry']['location']['lat'], x['geometry']['location']['lng'])).meters)
        stations['results'] = stations['results'][:3]

        # Process the stations
        evc_stations = []
        for place in stations['results']:
            temp_index += 1
            name = place['name']
            location = f"{place['geometry']['location']['lat']}, {place['geometry']['location']['lng']}"
            address = place['vicinity']
            num_chargers = randomize_chargers()  # Randomize the number of chargers
            max_loads = randomize_loads(num_chargers)  # Randomize the loads for each station
            current_load = 0
            station = Station(temp_index, name, address, location, num_chargers, max_loads, current_load)
            print(station)
            evc_stations.append(station)
            # # test for getter
            # stations_test = get_station_info()
            # print(stations_test)
            
            # print (evc_stations)

            # Check the type of current_load
            # print("Type of current_load:", type(current_load))


        break



    except Exception as e:
        print(f"Error retrieving places: {e}")
        print("An unexpected error occurred. Please try entering the location again or check your network connection.")


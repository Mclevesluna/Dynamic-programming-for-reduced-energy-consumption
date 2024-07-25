class Charger:
    def __init__(self, charger_type, availability, distance, time):
        self.charger_type = charger_type
        self.availability = availability
        self.distance = distance
        self.time = time

    def is_available(self):
        return self.availability

    def get_distance(self):
        return self.distance

    def get_time(self):
        return self.time

    def update_availability(self, availability):
        self.availability = availability

    def update_distance(self, distance):
        self.distance = distance

    def update_time(self, time):
        self.time = time

    def __str__(self):
        print("Charger type: {self.charger_type}, Availability: {self.availability}, Distance: {self.distance}, Time: {self.time}")


    # Create an instance of Charger
charger1 = Charger(charger_type="super charger", availability=True, distance=5.0, time=2.5)

# Calling methods
print("Availability:", charger1.is_available())
print("Distance:", charger1.get_distance())
print("Time:", charger1.get_time())

# Update charger information
charger1.update_availability(False)
charger1.update_distance(7.0)
charger1.update_time(3.0)

# Print updated information
print("Availability:", charger1.is_available())
print("Distance:", charger1.get_distance())
print("Time:", charger1.get_time())

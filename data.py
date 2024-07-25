import csv
import json

def csv_to_json(csv_file, json_file):
    print("Converting CSV to JSON...")
    # Open the CSV file for reading
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        # Convert each row to a dictionary and store in a list
        data = [row for row in csv_reader]
    print("CSV converted to JSON successfully.")

    print("Writing JSON data to file...")
    # Write the data to a JSON file
    with open(json_file, 'w') as file:
        # Use json.dump() to write data to the JSON file
        json.dump(data, file, indent=4)
    print("JSON data written to file:", json_file)

# Example usage
csv_to_json('EV_Database_UK.csv', './project/static/car_data.json')

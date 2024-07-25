function initMap() {
    const map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 51.5074, lng: -0.1278 }, // Default center (London)
        zoom: 12
    });

    // Simulated EV charging station data in London
    // Fetch the data from the JSON file
    fetch('static/data.json')
        .then(response => response.json())
        .then(data => {
            // Use the data to add markers to the map
            data.forEach(station => {
                new google.maps.Marker({
                    position: { lat: station.lat, lng: station.lng },
                    map: map,
                    title: station.name
                });
            });
        })
        .catch(error => {
            console.error('Error loading the station data:', error);
        });
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('static/car_data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('JSON data:', data);
            // Populate dropdown with data
            const dropdown = document.getElementById('carModel');
            if (!dropdown) {
                throw new Error('Dropdown element not found');
            }
            data.forEach(car => {
                const option = document.createElement('option');
                option.value = car.Cars;
                option.text = car.Cars;
                dropdown.appendChild(option);
            });

        })
        .catch(error => console.error('Error fetching the JSON file:', error));
});


document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').addEventListener('click', function() {
        fetch('static/data.json')
            .then(response => response.json())
            .then(data => {
                // Extract station names
                const stationNames = data.map(station => station.address);

                // Generate alert message dynamically
                const alertMessage = "Below are the three stations you can go to:\n" +
                                    stationNames.map((address, index) => (index + 1) + ". " + address).join("\n");

                // Randomly select one of the three stations for suggestion
                const randomStation = stationNames[Math.floor(Math.random() * stationNames.length)];

                // Add the suggestion to the alert message
                const finalAlertMessage = alertMessage + "\n\nWe suggest you to go to: " + randomStation + ", from the above 3 stations";

                // Show alert
                alert(finalAlertMessage);
            })
            .catch(error => {
                console.error('Error loading the station data:', error);
            });
    });
});



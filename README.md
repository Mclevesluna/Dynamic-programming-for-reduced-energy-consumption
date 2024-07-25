### ELECTRA

ELECTRA is a simulation tool designed to optimize the charging process for electric vehicles (EVs) using dynamic programming. The goal is to shift
towards smart charging by reducing current usage, maintaining minimum system load, and adjusting charging plans in real-time based on data inputs.

The problem identified is the carbon emissions offset by inefficient Electronic Vehicle charging are contributing to climate change. Our charging systems are inefficient, and it’s impacting our planet. Conventional EV charging in the UK relies on a grid that sources fossil fuel-based, solar, wind, etc. energy. This means we are ultimately charging our electronic vehicles with fossil fuels.

### Negative Impact on the Environment:
- **Higher Carbon Footprint**: Charging EVs with electricity derived from fossil fuels increases overall carbon emissions, undermining the environmental benefits of EVs.
- **Energy Source**: The conventional UK grid relies on fossil fuels for around 33% of electricity (as per UK Energy Trends March 2024).

### Negative Impact on EV Owners:
- **Battery Health**: Deterioration caused by overcharging reduces battery lifespan.
- **Wasted Time**: Inefficient charging systems lead to prolonged charging times.

### Our Proposed Solution
Software that shifts to smart charging with dynamic programming, uses less current, keeps the system at a reduced load, and adjusts charging plans with real-time data. This solution has the following impact metrics:
- **Reduces Energy Losses**: By charging at lower currents (optimal speed), balancing loads between stations, and making real-time adjustments as vehicles come in.
- **Reduced Carbon Emissions Linked to Energy Losses**: Minimizes losses by reducing charging power and calculating losses using real-time data.
- **Increase Battery Longevity**: By preventing overcharging.
- **Decrease Wait Times**: Ensures vehicles are ready and charged by the time the user needs to drive off.

Within the scope of the project, the first metric has been fully developed and included in the MVP. The other three metrics have an initial development but will be developed fully in the next product prototype.

## Body of Research

### Research and Realisation
While researching, we encountered a lot of information on the sustainability of electronic vehicles being less promising than expected, so we decided to tackle this problem. Our main insight was discovering that more renewable energy does not necessarily mean less carbon emissions because this reduction depends on the grid the energy is interacting with, not the source of the energy itself. That notion of a “clean” energy not being as clean as we might think led us to formulate our next hypothesis: If EVs in the UK are being charged on a grid heavily reliant on fossil fuels, then we are not even using renewable energy.

In the next stage of our research, we concentrated on the following points:
- How the energy grid in the UK works (charging in peak times, etc.).
- Effects of balancing an energy grid (UK or international case studies) - how it reduces carbon footprints, negative effects of having an imbalanced energy grid.
- ML approaches to energy loss reduction in the world - What has already been done? What have researchers already discovered?
- Things that have been done to reduce energy consumption (via charging) in the UK.
- How energy consumption translates into emissions in the UK.

### Creative Computational Exercise
The software developed uses the research previously mentioned to hit the four impact metrics described in the introduction in the following manner:
- **Optimal Charging Speed**: The algorithm uses an optimal charging speed for each vehicle instead of the maximum charging speed. Charging at optimal speeds can reduce energy losses, as losses are often proportional to the square of the current. By charging at lower currents (optimal speed), the algorithm reduces these losses.
- **Energy Loss Calculation**: Energy losses are calculated using a simplified model where losses are proportional to the square of the power (Ohm's Law). By reducing the charging power, the algorithm minimizes these losses.
- **Efficient Use of Time**: The algorithm allocates charging tasks based on the available time for each vehicle. It ensures that the vehicle charges within the available time frame, preventing overcharging and unnecessary energy consumption.
- **Balanced Load Distribution**: By checking the current load and maximum load of each station, the algorithm ensures that no station is overloaded. This balanced distribution of load helps in maintaining efficient energy use across all stations.
- **Real-time Adjustment**: The algorithm takes real-time data into account (e.g., current battery levels, available time, and current station load), allowing for dynamic adjustments and avoiding fixed schedules that might not be energy efficient.

## Technical Implementation

### Project Management, Development, and Deployment
We developed a main charging algorithm (`algorithm.py`) in Python to optimize charging and allocate charging tasks between stations. The following list details the step-by-step functioning of our software:

![ ](/Images/algorithmstructure.jpeg)

#### a) User Inputs:
- **Battery Level**: Current battery level of the EV.
- **Car Type**: Specific type of EV, as charging capabilities and battery sizes vary.
- **Current Location**: The user’s current location is used to find the nearest charging stations.
- **Maximum Duration**: The number of hours the user has to finish charging their car.

#### b) Finding Closest Charging Stations:
- **Google Maps API**: The software uses the Google Maps API to locate the nearest charging stations based on the user’s current location and preferences.

#### c) Charging Station Assignment:
- **Data Analysis**: The software analyzes the data to select the most suitable charging station considering factors like distance, availability, and charging speed.
- **Optimal Station**: Assign the EV to the nearest charging station that can charge the car within the user's maximum duration.

#### d) Charging Process:
- **Optimal Speed Charging**: The software controls the charging rate to optimize energy efficiency, charging the EV up to a maximum battery level of 80% to minimize energy loss.
- **Random Charging for Comparison**: Uses a random assignment and charging rate for comparative purposes to highlight the efficiency of the optimized process.

#### e) Energy Loss Reduction:
- **Efficiency Calculation**: The software calculates energy loss for both the optimized and random processes.
- **Comparison**: Compares the energy loss between the two methods, demonstrating the benefits of the optimized process.

#### f) User Feedback (using Flask):
- **Dashboard**: Users can view the charging status, energy savings, and efficiency comparisons.
- **Notifications**: Sends alerts and updates about the charging process and results.

### GUI and User Interface Development
This part is split in two for this project: 
1. The interface the user (EV owner looking to charge their car) sees and interacts with.
2. The GUI with the dashboard that our actual client (government or station owners) would see with all of their result metrics.

## Results  Technical Implementation
The use of this optimization algorithm could potentially reduce EV energy consumption in up to 70% after vehicle number 20.

![ ](/Images/chargingstations.png)
![ ](/Images/energylosses.png)

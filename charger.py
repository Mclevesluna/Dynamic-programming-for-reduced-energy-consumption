import random

def optimal_charging_rate(charging_speed, vehicle_type, current_battery_level,
                          max_vehicle_age=10, battery_degradation_rate=0.02,
                          temp_coeffs = [-0.02, 0.01], safety_margin=0.05):

    charging_speed = float(charging_speed)
    vehicle_age_years = random.uniform(0, max_vehicle_age)

    ambient_temperature = random.uniform(0, 35)

    if current_battery_level == 100:
            battery_temp_offset = 0.1
    else:
            battery_temp_offset = random.uniform(0, 15) * (current_battery_level / 100)

    current_temperature = ambient_temperature + battery_temp_offset

    temp_impact = temp_coeffs[0] * current_temperature + temp_coeffs[1] * current_temperature**2
    temp_factor = max(0, 1 - abs(temp_impact))
    temp_factor = float(temp_factor)

    health_factor = max(0, 1 - (vehicle_age_years * battery_degradation_rate))
    health_factor = float(health_factor)

    random_factor = random.uniform(0.95, 1.0)
    random_factor = float(random_factor)

    potential_optimal_speed = charging_speed * temp_factor * health_factor * random_factor
    optimal_charging_speed = min(potential_optimal_speed, charging_speed * (1 - safety_margin))

    min_charging_speed = 0.5
    optimal_charging_speed = max(optimal_charging_speed, min_charging_speed)

    return round(optimal_charging_speed, 2)

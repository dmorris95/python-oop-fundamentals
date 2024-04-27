#Task 1

from transportation import Bus

#create bus instances

bus1 = Bus("M23", "45")
bus2 = Bus("B11", "50")

print("City:",bus1.city_name,"\nBase fare:", bus1.base_fare)
print(f"Route Number: {bus1.route_number} holds {bus1.passenger_capacity} passengers.")

print("City:",bus2.city_name,"\nBase fare:", bus2.base_fare)
print(f"Route Number: {bus2.route_number} holds {bus2.passenger_capacity} passengers.")

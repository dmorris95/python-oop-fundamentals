class Bus:
    city_name = "Chicago"
    base_fare = "3.25"

    def __init__(self, route_number, passenger_capacity):
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity
        
        
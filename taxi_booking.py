from taxi import Taxi

class TaxiBooking:
    def __init__(self):
        self.taxi_list = []
        self.taxi_list_limit = 4
        self.id_generator = 1
        self.taxi_booked_history = []

    def book_taxi(self, pickup_location, drop_location, pickup_time):
        if len(self.taxi_list) < self.taxi_list_limit:
            self.taxi_list.append(Taxi(len(self.taxi_list) + 1))

        min_distance = float('inf')
        taxi_ready = None

        for taxi in self.taxi_list:
            if (taxi.drop_time is None or taxi.drop_time <= pickup_time) and \
               abs(ord(pickup_location) - ord(taxi.current_location)) <= min_distance:
                
                if abs(ord(pickup_location) - ord(taxi.current_location)) == min_distance:
                    if taxi_ready and taxi.earnings < taxi_ready.earnings:
                        taxi_ready = taxi
                else:
                    taxi_ready = taxi
                    min_distance = abs(ord(pickup_location) - ord(taxi.current_location))
        
        if taxi_ready:
            taxi_ready.customer_id = self.id_generator
            self.id_generator += 1
            taxi_ready.pickup_location = pickup_location
            taxi_ready.drop_location = drop_location
            taxi_ready.pickup_time = pickup_time
            travel_time = abs(ord(drop_location) - ord(pickup_location))
            taxi_ready.drop_time = pickup_time + travel_time
            fare = (travel_time * 15 - 5) * 10 + 100
            taxi_ready.earnings += fare
            taxi_ready.current_location = drop_location

            # Add to booking history (create a copy)
            self.taxi_booked_history.append(taxi_ready)

            return f"Taxi number {taxi_ready.taxi_id} is booked!"
        else:
            return "Taxis not available"

    def display_details(self):
        print("-----------------")
        for taxi in self.taxi_booked_history:
            print(taxi)
            print("-----------------")

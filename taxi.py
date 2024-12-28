class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.current_location = 'A'
        self.customer_id = None
        self.pickup_location = None
        self.drop_location = None
        self.pickup_time = None
        self.drop_time = None
        self.earnings = 0

    def __repr__(self):
        return (f"Taxi {self.taxi_id}\n"
                f"Current Location: {self.current_location}\n"
                f"Customer ID: {self.customer_id}\n"
                f"Pickup Location: {self.pickup_location}\n"
                f"Drop Location: {self.drop_location}\n"
                f"Pickup Time: {self.pickup_time}\n"
                f"Drop Time: {self.drop_time}\n"
                f"Earnings: {self.earnings}")

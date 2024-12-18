from transport.vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, capacity, is_refrigerated , current_load=0):
        super().__init__(capacity, current_load)
        self.is_refrigerated  = is_refrigerated 

    def __str__(self):
        return f"Van(ID: {self.vehicle_id}, Capacity: {self.capacity}, Current Load: {self.current_load},Is_refrigerated : {self.is_refrigerated })"
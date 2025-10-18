class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, capacity):
        """Initializes a Vehicle with a seating capacity."""
        self.capacity = capacity
        # Base cost for a generic vehicle
        self.base_fare = 100 
    
    def calculate_fare(self):
        """Calculates the basic fare for a vehicle."""
        return self.base_fare

class Bus(Vehicle):
    """Derived class representing a Bus."""
    
    def __init__(self, capacity):
        # Call the parent class's constructor
        super().__init__(capacity)
        # Surcharge specific to a bus (e.g., maintenance, comfort)
        self.bus_surcharge_rate = 0.10  # 10% surcharge
        
    def calculate_fare(self):
        """
        Calculates the total fare for the bus,
        including the base fare and a bus-specific surcharge.
        """
        # Get the base fare from the parent class
        base_fare = super().calculate_fare()
        
        # Calculate the surcharge amount
        surcharge = base_fare * self.bus_surcharge_rate
        
        # Total fare is base fare plus surcharge
        total_fare = base_fare + surcharge
        
        return total_fare

# Example Usage:

# Create a Bus instance with a capacity of 50
bus_9000 = Bus(capacity=50)

# Calculate and print the total fare
fare = bus_9000.calculate_fare()

print(f"Bus Capacity: {bus_9000.capacity} people")
print(f"Base Vehicle Fare: ${bus_9000.base_fare}")
print(f"Bus Surcharge Rate: {bus_9000.bus_surcharge_rate*100}%")
print(f"Total Bus Fare: ${fare}")
class Vehicle:
    """
    Base class representing a generic vehicle.
    The move() method is declared here to be overridden by subclasses.
    """
    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

class Helicopter(Vehicle):
    def move(self):
        print("Hovering 🚁")       

def perform_moves(vehicles):
    """
    Accepts a list of vehicles and calls the move() method on each,
    demonstrating polymorphism.
    """
    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    # Create instances of different vehicles
    my_car = Car()
    my_plane = Plane()
    my_boat = Boat()
    my_bicycle = Bicycle()
    my_helicopter = Helicopter()
    
    # Create a list of vehicles
    vehicles = [my_car, my_plane, my_boat, my_bicycle, my_helicopter]

    # Perform the move action on all vehicles, each outputting a unique action
    perform_moves(vehicles)

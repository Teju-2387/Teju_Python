class Vehicle:
    
    def start(self):
        print("Vehicle: Inside Vehicle CLass.")


class Car(Vehicle):

    def start(self):
    
        super().start()
        
        print("Car: Inside Car  Class")

if __name__ == "__main__":

    print("Calling start() on a Vehicle instance:")
    v = Vehicle()
    v.start()          # uses Vehicle.start()

    print("\nCalling start() on a Car instance:")
    c = Car()
    c.start()          # uses Car.start() → overrides and extends

    print("\nPolymorphic call via a base‑class reference:")

    v2: Vehicle = Car()  # Vehicle reference to a Car object
    v2.start()           # still calls Car.start() thanks to overriding

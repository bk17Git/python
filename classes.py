class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(5)

people = ["Harry", "Johny", "Ran", "Sam", "Jinks"]

for person in people:
    success = flight.add_passengers(person) 

    if success:
        print(f"Succesfully added {person} to the Flight!")
    else:
        print(f"Sorry,No seats {person} in the Flight")
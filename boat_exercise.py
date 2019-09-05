# Define a class called Boat
# Give it a method that allows the boat to move that prints 
# the speed at which it's moving.
# Define a Class called Kayak
# Make it a derived class of Boat
# Give it a method called paddle that uses its inherited move method.
# Make a Kayak instance and 'paddle' it


class Boat:
    def __init__(self, type, propulsion):
        self.type = type
        self.propulsion = propulsion

    def move(self, speed):
        print(f"The Boat is moving at {speed} miles per hour!")

class Kayak(Boat):
    def __init__(self, passengers=1):
        super().__init__("kayak", "paddle")
        self.passengers = passengers

    def paddle(self, speed=8):
        return self.move(speed)

cute_yellow_one = Kayak()
cute_yellow_one.paddle()

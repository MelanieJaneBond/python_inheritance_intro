# Create a Ford Mustang class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `fuel_capacity` attribute
#     * `gas_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `gas_level` by 4 each time it is invoked
#     * `refuel()` method method sets `gas_level` to `fuel_capacity` value

class Car:
    def __init__(self, manufacturer, model, fuel_capacity):
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.gas_level = 0
        self.horsepower = 400
        self.wheel_count = 4
    
    def drive(self, lowerby):
        self.gas_level -= lowerby
        print(f"You drove far enough! You only have {(self.gas_level) - 4} gallons left!")
    
    def refuel(self):
        self.gas_level = self.fuel_capacity
    
red_car = Car("Ford", "Mustang", 20)
red_car.refuel()
red_car.drive(5)

# Create a Dodge Ram class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `fuel_capacity` attribute
#     * `gas_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `gas_level` by 4 each time it is invoked
#     * `refuel()` method method sets `gas_level` to `fuel_capacity` value

class Pickup(Car):
    def __init__(self):
        super().__init__("Dodge", "Ram", 40)

blue_car = Pickup()
blue_car.refuel()
blue_car.drive(10)

# Steve designed it so that "super().__init__" came after each "drive" "refuel", etc. methods
# under the class Mustang(Vehicle):
# It looks like this:

# from vehicle import Vehicle

# class Mustang(Vehicle):

#     def __init__(self):
#         super().__init__("Mustang", "Ford", 40)

#     def drive(self):
#         super().drive(4)
    
#     def refuel(self):
#         self.gas_level = self.fuel_capacity

# Create a Nissan Leaf class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `battery_capacity` attribute
#     * `battery_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `battery_level` by 2 each time it is invoked
#     * `recharge()` method sets `battery_level` to `battery_capacity` value

# My attempt is below...
# class Leaf(Car):

#     def __init__(self):
#         super().__init__("Nissan", "Leaf", 11)
#         self.battery_capacity = self.fuel_capacity
#         self.battery_level = self.gas_level
    
#     def drive(self):
#         super().drive(2)

# It was a trick test; Steve wants us to realize that we need MULTIPLE inheritance!
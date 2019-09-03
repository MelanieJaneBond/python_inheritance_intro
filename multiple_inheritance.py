class Car:
    def __init__(self, manufacturer, model, hp, wheels):
        self.manufacturer = manufacturer
        self.model = model
        self.horsepower = hp
        self.wheel_count = wheels

# Steve has each of these class definitions in its own module.
# I would do that now but I am not certain I understand the dataflow
# enough yet to handle that structure/separation.
# It's nice to see the "inheritance" happening in one place first
# so that I can be certain I understand the syntax.

class GasPowered:
    def __init__(self, capacity):
        self.fuel_level = 0
        self.fuel_capacity = capacity
    
    def drive(self, lowerby):
        self.gas_level -= lowerby
        print(f"You drove far enough! You only have {self.gas_level} gallons left!")
    
    def refuel(self):
        self.gas_level = self.fuel_capacity
    
class ElectricPowered:
    def __init__(self, capacity):
        self.battery_level = 0
        self.battery_capacity = capacity
    
    def drive(self, lowerby):
        self.battery_level -= lowerby
        print(f"You drove far enough! You only have {self.battery_level} gallons left!")
    
    def refuel(self):
        self.battery_level = self.battery_capacity

class Leaf(Car, ElectricPowered):
    def __init__(self):
        Car.__init__(self, "Nissan", "Leaf", 50, 4)
        ElectricPowered.__init__(self, 45)

class Ram(Car, GasPowered):
    def __init__(self):
        Car.__init__(self, "Dodge", "Ram", 395, 4)
        GasPowered.__init__(self, 26)

class CrossTrek(Car, ElectricPowered, GasPowered):

    def __init__(self):
        Car.__init__(self, "CrossTrek", "Subaru", 60, 4)
        ElectricPowered.__init__(self, 40)
        GasPowered.__init__(self, 6)
    
    def refuel(self):
        ElectricPowered.refuel(self)
        GasPowered.refuel(self)
    
    def drive(self):
        ElectricPowered.drive(self, 3)
        GasPowered.drive(self, 0.5)


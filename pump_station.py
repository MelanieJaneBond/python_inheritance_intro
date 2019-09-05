class PumpStation:
    def __init__(self):
        self.__vehicles = []
    
    def add_vehicle(self, vehicle):
        try:
            if vehicle.gas_level > -1 and vehicle.fuel_capacity > -1:
                self.__vehicles.append(vehicle)
            except AttributeError:
                pass
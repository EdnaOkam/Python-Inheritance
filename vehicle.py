class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
    
    def display_info(self):
        print(f"Vehicle Make: {self.make} \nVehicle Model: {self.model} \nYear of Production: {self.year}")

class EngineMixin:
    def __init__(self, compression_ratio):
        self.compression_ratio = compression_ratio

    def display_info(self):
        print(f"Compression ratio of Vehicle: {self.compression_ratio}")

    def start_engine(self):
        print("Engine has started")

class ElectricMixin:
    def __init__ (self):
        self.charge_level = 0

    def charge(self,percentage):
        percentage = 100
        self.charge_level += percentage
        return percentage

class Car(Vehicle,EngineMixin):
    def __init__(self, make, model, year, nuum_doors, num_passengers):
        super().__init__(make, model, year)
        self.nuum_doors = nuum_doors
        self.num_passengers = num_passengers

    def display_info(self):
        super().display_info()
        print(f"Number of Doors in the Car: {self.nuum_doors} \nNumber of Passengers in the Car: {self.num_passengers}")

class ElectricCar(Car,ElectricMixin):
    def __init__(self, make, model, year, nuum_doors, num_passengers, battery_capacity):
        super().__init__(make, model, year, nuum_doors, num_passengers)
        ElectricMixin.__init__(self)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"The Battery Capacity of the Electric Car : {self.battery_capacity}")

class Motocycle(Vehicle,EngineMixin):
    def __init__(self, make, model, year, num_wheels, has_sidecar):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    
# car1 = Vehicle("BMW", "Turismo", 2020)
# car1.display_info()

engine_info = EngineMixin(10)
engine_info.display_info()
engine_info.start_engine()

car_info = Car("Nissan", "Altima", 2021, 4, 4,)
car_info.display_info()
# car_info.charge(75)

electric_car = ElectricCar("Mercedes", "Maybach",2022, 6, 4, "40kWh")
electric_car.display_info()
electric_car.charge(75)

moto1 = Motocycle("Ducati", "Alta", 2018, 2, True)
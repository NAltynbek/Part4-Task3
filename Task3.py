class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, km):
        self.odometer += km

    def __subtract_fuel(self, km):
        self.fuel -= km/10

    def drive(self, km):
        if (self.fuel - km/10) >= 0:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')

car = Car('Honda', 'Accord', 2009)
car.drive(650)
print(car.odometer, car.fuel)
car.drive(50)
print(car.odometer, car.fuel)
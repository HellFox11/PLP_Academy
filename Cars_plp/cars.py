
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.brand} {self.model} drives forward.")


class SportsCar(Car):
    def __init__(self, brand, model, year, top_speed):
        super().__init__(brand, model, year)
        self.__top_speed = top_speed 

    def drive(self):
        print(f"The {self.brand} {self.model} accelerates like lightning at {self.__top_speed} km/h!")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_range):
        super().__init__(brand, model, year)
        self.__battery_range = battery_range

    def drive(self):
        print(f"The {self.brand} {self.model} glides silently for {self.__battery_range} km.")


class SUV(Car):
    def __init__(self, brand, model, year, offroad_capable):
        super().__init__(brand, model, year)
        self.__offroad_capable = offroad_capable

    def drive(self):
        if self.__offroad_capable:
            print(f"The {self.brand} {self.model} climbs hills and crosses rivers effortlessly!")
        else:
            print(f"The {self.brand} {self.model} drives comfortably on the city roads.")

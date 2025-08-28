from cars import SportsCar, ElectricCar, SUV


ferrari = SportsCar("Ferrari", "488 Spider", 2022, 330)
tesla = ElectricCar("Tesla", "Model S", 2023, 600)
toyota = SUV("Toyota", "Land Cruiser", 2021, True)


cars = [ferrari, tesla, toyota]

for car in cars:
    car.drive()

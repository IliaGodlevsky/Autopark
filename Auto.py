PETROL_COST_PER_LITRE = 2.4
DIESEL_COST_PER_LITRE = 1.8


class Car:
    REDUCE_COST_EACH_INTERVAL = 1000
    ENHANCE_FUEL_CONSUMPTION = 1  # %

    def __init__(self, tank, car_cost, fuel_cost, service_cost, service_mileage):
        self.tank = tank
        self.car_cost = car_cost
        self. fuel_cost = fuel_cost
        self.__mileage = 0
        self.fuel_consumption = 0
        self.__max_mileage_to_service = 0
        self.service_cost = service_cost
        self.service_mileage = service_mileage


    def drive(self, distance):
        pass

    def service(self):
        pass


class DieselCar(Car):
    pass


class PetrolCar(Car):
    pass


class Factory:
    def __init__(self):
        self.produced = 0

    def produce(self, number):
        line_of_cars = []
        self.produced += number
        for it in range(0, number):
            if it % 3 == 0:
                if it % 5 == 0:
                    line_of_cars.append(DieselCar())
            else:
                line_of_cars.append(PetrolCar())
        return line_of_cars

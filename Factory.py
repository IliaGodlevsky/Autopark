import Constants as C
import PetrolCar as PC
import DieselCar as DC

class Factory:
    def __init__(self, number_of_cars=0):
        self.__number_of_cars = number_of_cars

    def new_plan(self, number_of_cars):
        self.__number_of_cars = number_of_cars

    def __produce_petrol_car_normal_tank(self):
        car1 = PC.PetrolCar(C.NORMAL_TANK, C.CAR_COST, C.PETROL_CAR_COST_LOSING, C.PETROL_COST, C.PETROL_FUEL_CONSUMPTION,
                        C.PETROL_SERVICE_COST, C.PETROL_MILEAGE_TILL_RECOVERY)
        return car1

    def __produce_petrol_car_better_tank(self):
        car2 = PC.PetrolCar(C.BETTER_TANK, C.CAR_COST, C.PETROL_CAR_COST_LOSING, C.PETROL_COST, C.PETROL_FUEL_CONSUMPTION,
                        C.PETROL_SERVICE_COST, C.PETROL_MILEAGE_TILL_RECOVERY)
        return car2

    def __produce_diesel_car_normal_tank(self):
        car3 = DC.DieselCar(C.NORMAL_TANK, C.CAR_COST, C.DIESEL_CAR_COST_LOSING, C.DIESEL_COST, C.DIESEL_FUEL_CONSUMPTION,
                        C.DIESEL_SERVICE_COST, C.DIESEL_MILEAGE_TILL_RECOVERY)
        return car3

    def __produce_diesel_car_better_tank(self):
        car4 = DC.DieselCar(C.BETTER_TANK, C.CAR_COST, C.DIESEL_CAR_COST_LOSING, C.DIESEL_COST, C.DIESEL_FUEL_CONSUMPTION,
                        C.DIESEL_SERVICE_COST, C.DIESEL_MILEAGE_TILL_RECOVERY)
        return car4

    def produce(self):
        auto_park = []
        for cycle in range(0, self.__number_of_cars):
            if cycle % 3 == 0 and cycle % 5 == 0:
                auto_park.append(self.__produce_diesel_car_better_tank())
            elif cycle % 3 == 0:
                auto_park.append(self.__produce_diesel_car_normal_tank())
            elif cycle % 5 == 0:
                auto_park.append(self.__produce_petrol_car_better_tank())
            else:
                auto_park.append(self.__produce_petrol_car_normal_tank())
        return auto_park

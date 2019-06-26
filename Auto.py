import random
import Car
import Factory as F
import Constants as C
import PetrolCar
import DieselCar


def extract(cars, type_of_car):
    park = []
    for car in cars:
        if isinstance(car, type_of_car):
            park.append(car)
    return park


def drive(cars, bottom, upper):
    for car in cars:
        car.drive(random.randrange(bottom, upper))
    return cars


def count_car_total_price(cars):
    total_price = Car.Car()
    for car in cars:
        total_price += car
    return total_price


factory = F.Factory(C.CAR_PRODUCTION)
my_cars = factory.produce()
my_cars = drive(my_cars, C.MIN_DISTANCE, C.MAX_DISTANCE)
petrol = extract(my_cars, PetrolCar.PetrolCar)
diesel = extract(my_cars, DieselCar.DieselCar)
petrol.sort()
diesel.sort()
summary = count_car_total_price(my_cars)
print(summary._car_cost)
for car in petrol: car.report()
for car in diesel: car.report()







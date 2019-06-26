from Functions import extract
import DieselCar as dc
import PetrolCar as pc
import Car
from random import randrange


class TaxiPark:
    def __init__(self, auto_park):
        self.__total_price = Car.Car()
        self.__auto_park = auto_park
        self.__petrol_cars = []
        self.__diesel_cars = []

    def send_in_way(self, bottom, upper):
        for car in self.__auto_park:
            car.drive(randrange(bottom, upper))

    def sort(self):
        self.sort_petrol_cars()
        self.sort_diesel_cars()

    def show_petrol_cars(self):
        for car in self.__petrol_cars:
            print("######################################")
            car.report()

    def show_diesel_cars(self):
        for car in self.__diesel_cars:
            print("######################################")
            car.report()

    def show_park(self):
        print("Petrol cars", "---------------------")
        self.show_petrol_cars()
        print("Diesel cars", "---------------------")
        self.show_diesel_cars()

    def sort_petrol_cars(self):
        self.__petrol_cars = extract(self.__auto_park, pc.PetrolCar)
        self.__petrol_cars.sort()

    def sort_diesel_cars(self):
        self.__diesel_cars = extract(self.__auto_park, dc.DieselCar)
        self.__diesel_cars.sort()

    def cars_total_price(self):
        self.__total_price = Car.Car()
        for car in self.__auto_park:
            self.__total_price += car
        return self.__total_price

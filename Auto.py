PETROL_COST = 2.4
DIESEL_COST = 1.8
NORMAL_TANK = 60
BETTER_TANK = 75
CAR_COST = 10000
PETROL_MILEAGE_TILL_RECOVERY = 100000
DIESEL_MILEAGE_TILL_RECOVERY = 150000
PETROL_SERVICE_COST = 500
DIESEL_SERVICE_COST = 700
PETROL_FUEL_CONSUMPTION = 8
DIESEL_FUEL_CONSUMPTION = 6
PETROL_CAR_COST_LOSING = 9.5
DIESEL_CAR_COST_LOSING = 10.5
FUEL_CONSUMPTION_INCREASE = 1.0
MILEAGE_TILL_GET_OLDER = 1000


class Report:
    pass


class Car:
    def __init__(self,
                 tank_capacity,
                 car_cost,
                 cost_losing,
                 fuel_cost,
                 fuel_consumption,
                 service_cost,
                 mileage_till_recovery):
        self.__tank_capacity = tank_capacity
        self.__current_tank_capacity = tank_capacity
        self.__car_cost = car_cost
        self.__cost_losing = cost_losing
        self.__fuel_cost = fuel_cost
        self.__fuel_consumption = fuel_consumption



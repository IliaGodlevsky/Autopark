# constants
PETROL_COST_PER_LITRE = 2.4
DIESEL_COST_PER_LITRE = 1.8
CAR_COST = 10000
REDUCE_COST_EACH_INTERVAL = 1000
NORMAL_TANK = 60
BETTER_TANK = 75
DIESEL_SERVICE_COST = 700
PETROL_SERVICE_COST = 500
DIESEL_SERVICE_MILEAGE = 150000
PETROL_SERVICE_MILEAGE = 100000
DIESEL_COST_LOSING = 10.5
PETROL_COST_LOSING = 9.5


class Report:
    def __init__(self):
        self.mileage = 0
        self.cost = 0
        self.cost_of_fuel_per_trip = 0
        self.tanked_up = 0
        self.mileage_till_recovery = 0

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_car_cost(self, car_cost):
        self.cost = car_cost

    def count_fuel_cost(self, tank_up_cost):
        self.cost_of_fuel_per_trip += tank_up_cost

    def tank_up(self):
        self.tanked_up += 1

    def set_recovery_mileage(self, mileage_till_recovery):
        self.mileage_till_recovery = mileage_till_recovery

    def report(self):
        pass


# base class
class Car:
    ENHANCE_FUEL_CONSUMPTION = 1  # %

    def __init__(self, tank, car_cost, fuel_cost, service_cost, service_mileage, cost_losing):
        self.board_computer = Report()
        self.__tank_capacity = tank
        self.tank = tank
        self.car_cost = car_cost
        self.fuel_cost = fuel_cost
        self.__mileage = 0
        self.__fuel_consumption = 0
        self.__max_mileage_to_service = 0
        self.service_cost = service_cost
        self.service_mileage = service_mileage
        self.cost_losing = cost_losing

    def drive(self, distance):
        for it in range(0, distance):
            self.__mileage += 1
            self.__fuel_burn_out()
            self.tank_up()
            self.enhance_car_cost(self.cost_losing)
            self.enhance_fuel_consumption(self.ENHANCE_FUEL_CONSUMPTION)
            self.service()
        return self.__mileage == distance

    def service(self):
        if self.__mileage % self.__max_mileage_to_service == 0:
            pass

    def enhance_fuel_consumption(self, value):
        if self.__mileage % REDUCE_COST_EACH_INTERVAL == 0:
            self.__fuel_consumption *= (1 + value/100)

    def enhance_car_cost(self, value):
        if self.__mileage % REDUCE_COST_EACH_INTERVAL == 0:
            self.car_cost -= value

    def __fuel_burn_out(self):
        self.tank -= self.__fuel_consumption/100

    def tank_up(self):
        if self.tank == 0:
            self.tank = self.__tank_capacity

    def report(self):
        self.board_computer.report()


class PetrolCar(Car):

    def __gt__(self, other):
        return self.__max_mileage_to_service > other.__max_mileage_to_service

    def __lt__(self, other):
        return not self < other


class DieselCar(Car):

    def __gt__(self, other):
        return self.car_cost > other.car_cost

    def __lt__(self, other):
        return not self < other


class Factory:
    def __call__(self, quantity_of_cars):
        for it in range(0, quantity_of_cars):
            if it % 3 == it % 5:
                return DieselCar(BETTER_TANK, CAR_COST, DIESEL_COST_PER_LITRE,
                                 DIESEL_SERVICE_COST, DIESEL_SERVICE_MILEAGE, DIESEL_COST_LOSING)
            elif it % 3 == 0:
                return DieselCar(NORMAL_TANK, CAR_COST, DIESEL_COST_PER_LITRE,
                                 DIESEL_SERVICE_COST, DIESEL_SERVICE_MILEAGE, DIESEL_COST_LOSING)
            elif it % 5 == 0:
                return PetrolCar(BETTER_TANK, CAR_COST, PETROL_COST_PER_LITRE,
                                 PETROL_SERVICE_COST, PETROL_SERVICE_MILEAGE, PETROL_COST_LOSING)
            else:
                return PetrolCar(NORMAL_TANK, CAR_COST, PETROL_COST_PER_LITRE,
                                 PETROL_SERVICE_COST, PETROL_SERVICE_MILEAGE, PETROL_COST_LOSING)

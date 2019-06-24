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
        print("Mileage is: ", self.mileage)
        print("Cost remained: ", self.cost)
        print("Spent on fuel: ", self.cost_of_fuel_per_trip)
        print("Tanked up: ", self.tanked_up)
        print("Mileage till recovery: ", self.mileage_till_recovery)


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
        self.__fuel_consumption = 8.4
        self.__max_mileage_to_service = 150000
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
        self.board_computer.set_car_cost(self.car_cost)
        self.board_computer.set_mileage(self.__mileage)
        self.board_computer.set_recovery_mileage((self.mileage_till_recovery()))
        return self.__mileage == distance

    def mileage_till_recovery(self):
        mileage = self.__mileage
        while mileage - self.__max_mileage_to_service >= 0:
            mileage -= self.__max_mileage_to_service
        return mileage

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
            self.board_computer.tank_up()
            self.board_computer.count_fuel_cost(self.__tank_capacity * self.fuel_cost)

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


# class Factory:
#     def produce_cars(self, quantity_of_cars=100):
#         park_of_petrols = []
#         park_of_diesels = []
#         auto_park = [park_of_petrols, park_of_diesels]
#         for it in range(0, quantity_of_cars):
#             if it % 3 == it % 5:
#                 auto_park[1].append(DieselCar(BETTER_TANK, CAR_COST, DIESEL_COST_PER_LITRE, DIESEL_SERVICE_COST,DIESEL_SERVICE_MILEAGE, DIESEL_COST_LOSING))
#             elif it % 3 == 0:
#                 auto_park[1].append(DieselCar(NORMAL_TANK, CAR_COST, DIESEL_COST_PER_LITRE, DIESEL_SERVICE_COST,DIESEL_SERVICE_MILEAGE, DIESEL_COST_LOSING))
#             elif it % 5 == 0:
#                 auto_park[0].append(PetrolCar(BETTER_TANK, CAR_COST, PETROL_COST_PER_LITRE, PETROL_SERVICE_COST,PETROL_SERVICE_MILEAGE, PETROL_COST_LOSING))
#             else:
#                 auto_park[0].append(PetrolCar(NORMAL_TANK, CAR_COST, PETROL_COST_PER_LITRE, PETROL_SERVICE_COST,PETROL_SERVICE_MILEAGE, PETROL_COST_LOSING))
#         return auto_park


# factory = Factory()
# auto_park = factory.produce_cars()
# for car in auto_park[0]:
#     car.drive(55000)
# for car in auto_park[1]:
#     car.drive(200000)


# auto_park[1][0].report()

car = PetrolCar(NORMAL_TANK, CAR_COST, PETROL_COST_PER_LITRE, PETROL_SERVICE_COST,PETROL_SERVICE_MILEAGE,
                PETROL_COST_LOSING)
car1 = car
car.drive(100000)
car.report()







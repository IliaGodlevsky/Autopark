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
STOP = False
GO = True


class Report:
    def __init__(self):
        self.__mileage = 0
        self.__cost_remain = 0
        self.__total_fuel_cost = 0
        self.__times_of_tanking_up = 0
        self.__mileage_to_recovery = 0

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_mileage_to_recovery(self, mileage_till_recovery):
        self.__mileage_to_recovery = mileage_till_recovery - self.__mileage % mileage_till_recovery

    def set_remaining_cost(self, cost_remain):
        self.__cost_remain = cost_remain

    def count_fuel_cost(self, fuel_cost):
        self.__total_fuel_cost += fuel_cost

    def tanked_up(self):
        self.__times_of_tanking_up += 1

    def report(self):
        print("Total mileage: ", self.__mileage)
        print("Cost remained: ", self.__cost_remain)
        print("Fuel expends: ", self.__total_fuel_cost)
        print("Tanked up, times: ", self.__times_of_tanking_up)
        print("Mileage to next recovery: ", self.__mileage_to_recovery)


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
        self._car_cost = car_cost
        self.__cost_losing = cost_losing
        self.__fuel_cost = fuel_cost
        self.__fuel_consumption = fuel_consumption
        self.__start_fuel_consumption = fuel_consumption
        self.__service_cost = service_cost
        self.__mileage_till_recovery = mileage_till_recovery
        self.__mileage = 0
        self.__board_computer = Report()

    def drive(self, distance):
        while self.__mileage < distance:
            self.__mileage += 1
            self.__fuel_consume()
            self.__tank_up()
            self.__increase_fuel_consumption()
            self.__reduce_cost()
            self.__service()
        self.__board_computer.set_mileage(self.__mileage)
        self.__board_computer.set_remaining_cost(self._car_cost)
        self.__board_computer.set_mileage_to_recovery(self.__mileage_till_recovery)

    def __fuel_consume(self):
        self.__current_tank_capacity -= self.__fuel_consumption/100.0

    def __increase_fuel_consumption(self):
        if self.__mileage % MILEAGE_TILL_GET_OLDER == 0:
            self.__fuel_consumption += self.__start_fuel_consumption * (FUEL_CONSUMPTION_INCREASE/100.0)

    def __reduce_cost(self):
        if self.__mileage % MILEAGE_TILL_GET_OLDER == 0:
            self._car_cost -= self.__cost_losing

    def __out_of_fuel(self):
        return self.__current_tank_capacity <= 0

    def __tank_up(self):
        if self.__out_of_fuel():
            self.__current_tank_capacity = self.__tank_capacity
            self.__board_computer.count_fuel_cost(self.__tank_capacity * self.__fuel_cost)
            self.__board_computer.tanked_up()

    def __service(self):
        if self.__mileage % self.__mileage_till_recovery == 0:
           return True

    def report(self):
        self.__board_computer.report()

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass


class DieselCar(Car):
    def __init__(self, tank_capacity,
                 car_cost,
                 cost_losing,
                 fuel_cost,
                 fuel_consumption,
                 service_cost,
                 mileage_till_recovery):
        super().__init__(tank_capacity, car_cost, cost_losing, fuel_cost, fuel_consumption, service_cost,
                         mileage_till_recovery)

    def __gt__(self, other):
        return self._car_cost > other._car_cost

    def __lt__(self, other):
        return self._car_cost < other._car_cost


car = DieselCar(BETTER_TANK, CAR_COST, DIESEL_CAR_COST_LOSING,
                DIESEL_COST, DIESEL_FUEL_CONSUMPTION,
                DIESEL_SERVICE_COST, DIESEL_MILEAGE_TILL_RECOVERY)
car2 = DieselCar(BETTER_TANK, CAR_COST, PETROL_CAR_COST_LOSING, DIESEL_COST, DIESEL_FUEL_CONSUMPTION,DIESEL_SERVICE_COST, DIESEL_MILEAGE_TILL_RECOVERY)

car.drive(20000)
car2.drive(20000)

better = car2 > car
print(better)



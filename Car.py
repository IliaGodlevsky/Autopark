import Constants
import Report


class Car:
    def __init__(self,
                 tank_capacity=0,
                 car_cost=0,
                 cost_losing=0.0,
                 fuel_cost=0.0,
                 fuel_consumption=0,
                 service_cost=0,
                 mileage_till_recovery=0):
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
        self._board_computer = Report.Report()

    def drive(self, distance):
        interval = 100
        first_distance = distance - distance % 100
        self.__move(first_distance, interval)
        if distance % 100 != 0:
            second_distance = distance + distance - first_distance
            interval = 1
            self.__move(second_distance, interval)
        self._board_computer.set_mileage(self.__mileage)
        self._board_computer.set_remaining_cost(self._car_cost)
        self._board_computer.set_mileage_to_recovery(self.__mileage_till_recovery)
        self._board_computer.fuel_info(self.__current_tank_capacity)

    def __move(self, distance, interval):
        while self.__mileage < distance:
            self.__mileage += interval
            self.__fuel_consume(self.__fuel_consumption/100 * interval)
            self.__tank_up()
            self.__increase_fuel_consumption()
            self.__reduce_cost()
            self.__service()

    def __fuel_consume(self, fuel_consume):
        self.__current_tank_capacity -= fuel_consume

    def __increase_fuel_consumption(self):
        if self.__mileage % Constants.MILEAGE_TILL_GET_OLDER == 0:
            self.__fuel_consumption += self.__start_fuel_consumption * (Constants.FUEL_CONSUMPTION_INCREASE/100.0)

    def __reduce_cost(self):
        if self.__mileage % Constants.MILEAGE_TILL_GET_OLDER == 0:
            self._car_cost -= self.__cost_losing

    def __out_of_fuel(self):
        return self.__current_tank_capacity <= 0

    def __tank_up(self):
        if self.__out_of_fuel():
            self._board_computer.count_fuel_cost((self.__tank_capacity - self.__current_tank_capacity) * self.__fuel_cost)
            self.__current_tank_capacity = self.__tank_capacity
            self._board_computer.tanked_up()

    def __service(self):
        if self.__mileage % self.__mileage_till_recovery == 0:
            self._board_computer.count_recovery_expends(self.__service_cost)

    def report(self):
        self._board_computer.report()

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __add__(self, other):
        return Car(0, self._car_cost + other._car_cost, 0, 0, 0, 0, 0)

    def __iadd__(self, other):
        self._car_cost += other._car_cost
        return self

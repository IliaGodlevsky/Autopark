

class Report:
    def __init__(self):
        self.__mileage = 0
        self.__cost_remain = 0
        self.__total_fuel_cost = 0
        self.__times_of_tanking_up = 0
        self.__mileage_to_recovery = 0
        self.__recovery_expends = 0

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_mileage_to_recovery(self, mileage_till_recovery):
        self.__mileage_to_recovery = mileage_till_recovery - self.__mileage % mileage_till_recovery

    def set_remaining_cost(self, cost_remain):
        self.__cost_remain = cost_remain

    def count_recovery_expends(self, expends):
        self.__recovery_expends += expends

    def count_fuel_cost(self, fuel_cost):
        self.__total_fuel_cost += fuel_cost

    def tanked_up(self):
        self.__times_of_tanking_up += 1

    def mileage_to_recovery(self):
        return self.__mileage_to_recovery

    def report(self):
        print("Total mileage: ", self.__mileage)
        print("Cost remained: ", self.__cost_remain)
        print("Fuel expends: ", self.__total_fuel_cost)
        print("Tanked up, times: ", self.__times_of_tanking_up)
        print("Mileage to next recovery: ", self.__mileage_to_recovery)
        print("Recovery expends: ", self.__recovery_expends)


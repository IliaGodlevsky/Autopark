import Car


class PetrolCar(Car.Car):
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
        return self._board_computer.mileage_to_recovery() > other._board_computer.mileage_to_recovery()

    def __lt__(self, other):
        return not self > other
import Car


class DieselCar(Car.Car):
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
import Factory as F
import Constants as C
import Taxipark as taxi

factory = F.Factory(C.CAR_PRODUCTION)
my_cars = factory.produce()
taxi_park = taxi.TaxiPark(my_cars)
taxi_park.send_in_way(C.MIN_DISTANCE, C.MAX_DISTANCE)
taxi_park.sort()
taxi_park.show_park()
print("Taxi park cars total cost: ", taxi_park.cars_total_price())









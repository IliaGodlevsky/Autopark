# extracts a type from list of items
def extract(cars, type_of_car):
    park = []
    for car in cars:
        if isinstance(car, type_of_car):
            park.append(car)
    return park

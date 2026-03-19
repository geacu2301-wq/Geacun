class Car:
    def __init__(self, car_number, maximum_speed):
        self.car_number = car_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
car = Car("1234", 200)
print(car, car.car_number, car.maximum_speed, car.current_speed, car.travelled_distance)
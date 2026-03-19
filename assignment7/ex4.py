import random
class Car:
    def __init__(self, car_number, max_speed):
        self.car_number = car_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
cars = []
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))
race_over = False
while not race_over:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_over = True
print(f"{'Car':<10} {'Max':<10} {'Speed':<10} {'Distance':<10}")
for car in cars:
    print(f"{car.car_number:<10} "
          f"{car.max_speed:<10} "
          f"{car.current_speed:<10} "
          f"{car.travelled_distance:<10.2f}")
        
        
        
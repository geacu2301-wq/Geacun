
import random
class Car:
    def __init__(self, reg_number, highest_speed):
        self.reg_number = reg_number
        self.max_speed = highest_speed   
        self.speed = 0
        self.distance = 0
    def accelerate(self, speed_decrease_increase):
        self.speed += speed_decrease_increase
        if self.speed > self.max_speed:  
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0
    def drive(self, hours):
        self.distance += self.speed * hours
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
    def print_status(self):
        print("\nRACE STATUS")
        print(f"{'Car':<10}{'Speed(km/h)':<15}{'Distance(km)':<15}")
        for car in self.cars:
            print(f"{car.reg_number:<10}{car.speed:<15}{car.distance:<15.1f}")
    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False
cars = []
for i in range(10):
    reg = f"ABC-{i+1}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))
race = Race("Grand Demolition Derby", 8000, cars)
hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\nHour: {hours}")
        race.print_status()
print("\n the end of reuslut:")
race.print_status()

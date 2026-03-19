class car:
    def __init__(self, max_speed):
        self.speed=0
        self.max_speed=max_speed
        self.distance=0
        def control(self, hours):
            self.distance+=self.speed*hours
            car=car(180)
            car.speed=30
            car.distance=2000
            car.control(1.5)
            print("Current distance:",car.distance)
            
            

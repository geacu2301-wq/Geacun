class Building:
    def __init__(self, middle, top, num_elevators):
        self.bottom = middle
        self.top = top
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(middle, top))
    def run_elevator(self, elevators_number, destination):
        print(f"\nRunning elevator {elevators_number} to floor {destination}")
        self.elevators[elevators_number].go_to_floor(destination)
    def fire_alarm(self):
        print("\n FIRE ALARM ACTIVATED! All elevators go to bottom of floor!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)
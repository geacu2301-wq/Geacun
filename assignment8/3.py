class Elevator:
    def __init__(self, peak, top):
        self.bottom = peak
        self.top = top
        self.current_floor =peak
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.peak:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")
    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
class Building:
    def __init__(self, peak, top, number_of_elevators):
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(peak, top))
    def run_elevator(self, elevator_number, target_floor):
        self.elevators[elevator_number].go_to_floor(target_floor)
    def fire_alarm(self):
        print("\n  ALARM ACTIVATED ")
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.peak)
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def acc(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
new_car = Car("ABC-123", 150)
new_car.acc(30)
new_car.acc(70)
new_car.acc(50)
print(f"Current speed after acceleration: {new_car.current_speed} km/h")
new_car.acc(-200)
print(f"Final speed after emergency brake: {new_car.current_speed} km/h")
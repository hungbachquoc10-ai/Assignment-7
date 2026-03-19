class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed = max(0, min(self.max_speed, self.current_speed + change))
    def drive(self, hours):
        if hours > 0:
            distance_to_add = self.current_speed * hours
            self.travelled_distance += distance_to_add
car = Car("ABC-123", 142)
car.travelled_distance = 2000
car.current_speed = 60
print(f"Distance before: {car.travelled_distance} km") 
car.drive(1.5)
print(f"Distance after: {car.travelled_distance} km")


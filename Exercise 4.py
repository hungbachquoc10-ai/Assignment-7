import random
class Car:
    def __init__(self, reg_number, max_speed):
        self.registration_number = reg_number
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
    reg_num = f"ABC-{i}"
    max_spd = random.randint(150, 200)
    cars.append(Car(reg_num, max_spd))
race_on = True
hour_count = 0
while race_on:
    hour_count += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_on = False
print(f"{'Reg. Number':<12} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance (km)':<15}")
print("-" * 60)
for car in cars:
    print(f"{car.registration_number:<12} | {car.max_speed:<10} | {car.current_speed:<15} | {car.travelled_distance:<15.1f}")
print(f"Race finished after {hour_count} hours.")
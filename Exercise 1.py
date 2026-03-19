class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
if __name__ == "__main__":
    reg_num = input("Car's registration number: ")
    max_spd = input("Car's maximum speed (km/h): ")
    user_car = Car(reg_num, int(max_spd))
    print("New Car Created:")
    print(f"Registration number: {user_car.reg_number}")
    print(f"Maximum speed:       {user_car.max_speed} km/h")
    print(f"Current speed:       {user_car.current_speed} km/h")
    print(f"Travelled distance:  {user_car.travelled_distance} km")
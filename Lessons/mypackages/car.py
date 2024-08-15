# Define a clas car ( this would be part of our lesson 13 and 14)

class Car:
    def __init__(self, number_doors,registration_number,make,model,year,max_speed,acceleration_rate,deceleration_rate) -> None:
        self.number_doors = number_doors
        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.acceleration_rate = acceleration_rate
        self.deceleration_rate = deceleration_rate
        self.mileage_miles = 0
        self.speed_mph = 0
    def __str__(self) -> str:
        return f"Car{{'number_doors': {self.number_doors}, 'registration_number': '{self.registration_number}', 'make': '{self.make}', 'model': '{self.model}', 'year_manufactured': {self.year}, 'maximum_speed': {self.max_speed}, 'acceleration_rate': {self.acceleration_rate}, 'deceleration_rate': {self.deceleration_rate}, 'mileage_miles': {self.mileage_miles}, 'speed_mph': {self.speed_mph}}}" 
    
    def accelerate(self) -> None:
        print(f"{self.make} {self.model} accelerating . . .")



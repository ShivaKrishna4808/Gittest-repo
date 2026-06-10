class vehicle:
    def start(self):
        return "Vehicle stars"
    
class Car(vehicle):
    def start(self):
        return 'Car starts'
    
class sportscar(Car):
    def start(self):
        return "Sports car starts"
    
sports_car = sportscar()
print(sports_car.start())
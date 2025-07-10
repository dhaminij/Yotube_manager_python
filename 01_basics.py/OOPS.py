# craete a car class with attributes like brand and model
#  then create instance of this class

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
        

class ElectricCar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize =batterysize

# my_tesla = electr
my_car = Car("swift","corlla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())


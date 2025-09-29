#Classes:
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def rollover(self):
        print(f"{self.name.title()} is rolls over.")

    def sit(self):
        print(f"{self.name.title()} is sitting.")

my_dog=Dog('Willie',16)
print(f"My dog name is {my_dog.name.title()} and age is {my_dog.age}")
my_dog.sit()
my_dog.rollover()

your_dog=Dog('Rocky',7)
print(f"Your dog name is {your_dog.name.title()} and age is {your_dog.age}")
your_dog.sit()
your_dog.rollover()

#Car class:
class Car:
    def __init__(self,name,model_no,manufactured_date):
        self.name=name
        self.model_no=model_no
        self.manufactured_data=manufactured_date
        self.odometer=0

    def get_descriptivename(self):
        long_name=f"{self.name} {self.model_no} {self.manufactured_data}"
        return long_name
    
    def display_odometer(self):
        print(f"Odometer reading is {self.odometer}")

    def update_odometer(self,mileage):
        self.odometer=mileage
    
    def increase_odometer(self,miles):
        self.odometer+=miles
    
my_car=Car('audi','A176',2019)
print(my_car.get_descriptivename())
my_car.update_odometer(23500)
my_car.increase_odometer(100)
my_car.display_odometer()

#inheritance:
class Electric_cars(Car):
    def __init__(self, name, model_no, manufactured_date):
        super().__init__(name, model_no, manufactured_date)
        self.battery_size=75
    
    def describe_batterysize(self):
        print(f"The size of battery is {self.battery_size}")

my_tesla=Electric_cars('Tesla','Z',2019)
print(f"{my_tesla.get_descriptivename()}")
my_tesla.describe_batterysize()
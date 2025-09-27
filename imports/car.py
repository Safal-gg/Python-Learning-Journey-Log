"""A class that can be used to represent a car."""

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

class Electric_cars(Car):
    def __init__(self, name, model_no, manufactured_date):
        super().__init__(name, model_no, manufactured_date)
        self.battery_size=75
    
    def describe_batterysize(self):
        print(f"The size of battery is {self.battery_size}")
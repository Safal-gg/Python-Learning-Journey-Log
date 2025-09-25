#instances as attribute:
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
    
class Battery:
    def __init__(self,battery_size):
        self.battery_size=battery_size

    def describe_batterysize(self):
        print(f"The size of battery is {self.battery_size}")

    def get_range(self):
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=310
        print(f"{range} is the range of the car.")

    def upgrade_battery(self):
        if self.battery_size<100:
            self.battery_size=100
        

        
class Electric_cars(Car):
    def __init__(self, name, model_no, manufactured_date):
        super().__init__(name, model_no, manufactured_date)
        self.battery=Battery(75)
    
my_tesla=Electric_cars('Tesla','Z',2019)
my_tesla.battery.describe_batterysize()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
    
   


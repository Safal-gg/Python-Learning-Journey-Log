from car import Car as C,Electric_cars as E


my_car=C('Audi','A1',2020)
print(f"{my_car.get_descriptivename()}")

my_ecar=E('Tesla','S',2019)
print(f"{my_ecar.get_descriptivename()}")
my_ecar.describe_batterysize()
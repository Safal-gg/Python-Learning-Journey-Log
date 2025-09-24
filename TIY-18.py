#sandwiches:
def sandwhich_toppings(toppings):
    for topping in toppings:
        print(topping.title())

sandwhich_items=['tomatoes','cheese','mayo','lettuce']
sandwhich_toppings(sandwhich_items)

#cars:
def make_car(manufacturer,model_name,**car_info):
    car_info['Manufacturer']=manufacturer
    car_info['Model name']=model_name
    return car_info

car=make_car('subaru','A134',color='purple',tow_package=True)

print(car)
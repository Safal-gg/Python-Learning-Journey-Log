#Ice Cream Stand:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"Name:{self.restaurant_name.title()} & Cuisine type:{self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

restaurant=Restaurant('Trisara','momo')
print(f"The name of the restaurant is {restaurant.restaurant_name.title()} and its main cuisine is {restaurant.cuisine_type.title()}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2=Restaurant('marget','pizza')
restaurant_2.describe_restaurant()
restaurant_3=Restaurant('indies','burger')
restaurant_3.describe_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='icecream'):
        super().__init__(restaurant_name, cuisine_type)
        self.icecream_flavors=''

    def display_icecream(self):
        print(f"The flavor of icecream is {self.icecream_flavors.title()}")

icecream=IceCreamStand('Dens')
icecream.describe_restaurant()
icecream.icecream_flavors='vanilla'
icecream.display_icecream()

#Admin:
class User:
    def __init__(self,first_name,last_name,gender,age,profession):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.age=age
        self.profession=profession
        self.login_attempts=0
    
    def describe_user(self):
        print(f"Name:{self.first_name.title()} {self.last_name.title()}\n")
        print(f"Gender:{self.gender.title()}, Age:{self.age}\n")
        print(f"Profession:{self.profession.title()}")
    
    def greet_user(self):
        print(f"Hello! {self.first_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

user_1=User('john','pradhan','male',23,'doctor')
user_2=User('safal','shrestha','male',19,'engineer')
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()

user_1.increment_login_attempts()
print(f"{user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"{user_1.login_attempts}")


class Privileges:
    def __init__(self):
         self.privileges=['can add post','can delete post','can ban user','can kick user']
        
    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, gender, age, profession):
        super().__init__(first_name, last_name, gender, age, profession)
        self.pri=Privileges()
       

admin=Admin('albert','einstein','male',44,'scientist')
admin.describe_user()
admin.pri.show_privileges()
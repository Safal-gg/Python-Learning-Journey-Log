#Number served:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"Name:{self.restaurant_name.title()} & Cuisine type:{self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

    def display_numberserved(self):
        print(f"Number served is {self.number_served}")

    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self,number):
        self.number_served += number

restaurant=Restaurant('Trisara','momo')
print(f"The name of the restaurant is {restaurant.restaurant_name.title()} and its main cuisine is {restaurant.cuisine_type.title()}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(23)
restaurant.increment_number_served(100)
restaurant.display_numberserved()

restaurant_2=Restaurant('marget','pizza')
restaurant_2.describe_restaurant()
restaurant_3=Restaurant('indies','burger')
restaurant_3.describe_restaurant()

#ULogin attempts:
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
#Pizza Toppings:
pizza_toppings=""
flag=True
while flag==True:
    pizza_toppings=input('enter your favorite pizza toppings')
    if pizza_toppings=='quit':
        flag=False
    else:
        print(f"I will add {pizza_toppings.title()} to the menue")

#movie tickets:
active=True
while active:
    age=input("enter your age for the movie tickets")
    age=int(age)
    if age<3:
        print("the ticket is free")
    elif age>=3 and age<12:
        print("the ticket is $10")
    elif age>12:
        print("the ticket is $15")
    message=input("do you still want to continue?(Y/N)")

    if message.lower()=="n":
        active=False

#Using Break:

while True:
    age=input("enter your age for the movie tickets and type quit if you want to exit ")
    if age=='quit':
        break
    age=int(age)
    
    if age<3:
        print("the ticket is free")
    elif age>=3 and age<12:
        print("the ticket is $10")
    elif age>12:
        print("the ticket is $15")
    
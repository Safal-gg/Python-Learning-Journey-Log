#Rental Car:
rental_car=input("What rental car you would like?")
print(f"Lets me see if I can find you a {rental_car.title()}")

#Restaurant Seating:
people=input("How many people are in their dinner group?:")
people=int(people)
if people<8:
    print("Your table is ready!")
else:
    print("Your group will have to wait")

#Multiples of Ten:
number=input("enter any number:")
number=int(number)

if number%10==0:
    print("the number is multiple of 10")

else:
    print("the number is not multiple of 10")
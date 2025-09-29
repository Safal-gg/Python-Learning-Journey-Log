#using range() function 
for value in range(1,6): #1 to 6 because of off by one behaviour
    print(value)

#using range() function in a list
numbers=list(range(1,6))
print(numbers)

#adding third argument as a step size
even_numbers=list(range(2,9,2))
print(even_numbers)

#simple statistics with a list of numbers
digits=[1,2,3,4,5,6,7,8,9,10]
x=max(digits)
print(x)
y=min(digits)
print(y)
z=sum(digits)
print(z)

#slicing a list
names=['hari','safal','ram','ramesh']
print(names[0:3])

#looping through a slice
for name in names[:3]:
    print(name.title())

#tuple
dimensions=(200,50)
print(dimensions)

#looping in tuple
for dimension in dimensions:
    print(dimension)

#writing over tuple
dimensions=(400,50)
print(dimensions)

#if-else statement
cars=['bmw','audi','ford']

for car in cars:
    if car=='bmw':
        print(car.upper())
    
    else:
        print(car.title())


#if-elif-else statement

ages=[18,19,27,4,3,2]

for age in ages:
    if age<=4:
        print("Your entrance fee is $0")
    elif age<=18:
        print("your entrance fee is $5")
    else:
        print("Your entrance fee is $10")


#multiple if

requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

   

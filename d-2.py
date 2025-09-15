#Names of friends with greetings.
names=['ronish','vision','onyx','rishabh']
print("1st name is:",names[0].title())
print("2nd name is:",names[1].title())
print("3rd name is:",names[2].title())
print("4th name is:",names[3].title())

#Your own list.
transportation=['motorcycle','car','aeroplane']
message1=f"I would like to own a honda {transportation[0].title()}"
message2=f"I would like to own a porche {transportation[1].title()}"
message3=f"I would like to own a private {transportation[2].title()}"

print(message1)
print(message2)
print(message3)

#changing the element in the list

transportation[0]='tank'
print(transportation)

#adding an element to the list

#append(adds an element automatically at the end of the list)
transportation.append('boat')
print(transportation)

#insert(adds an element at any position by specifying the index of the new element )
transportation.insert(0,'horse')
print(transportation)

#deleting element from the list using del command
del transportation [0]
print(transportation)

#popping out element from the list using pop-method
x=transportation.pop(0)
print(transportation)
print(x)

#removing an item by value
transportation.remove('aeroplane')
print(transportation)
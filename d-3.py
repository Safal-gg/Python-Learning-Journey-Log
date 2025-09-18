#sorting lists
bikes=['yamaha','ducati','kawasaki']
bikes.sort()
print(bikes)

#sorting in reverse order
bikes.sort(reverse=True)
print(bikes)

#sorting temporarily
cars=['ford','audi','bugati']
print("Unsorted list is:",cars)
print("Sorted list is:",sorted(cars))
print("Unsorted list is:",cars)
print("Reverse Sorted list is:",sorted(cars,reverse=True))

#reverse() method reversing the list not in alphabetical order but simply reversing the element in the list

names=['safal','vision','ronish','onyx']
names.reverse()
print(names)

#finding the length of the list using len() function.

print(len(names))

#looping through an entire list
magicians=['david','alice','mark']
for magician in magicians:
    print(magician)

#doing more work within a for loop
for magician in magicians:
    print(f"{magician.title()},you have done a great trick!")
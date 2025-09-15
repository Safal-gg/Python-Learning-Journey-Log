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
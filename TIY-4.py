#counting to twenty
for value in range(1,21):
    print(value)

#one million
numbers=list(range(1,1000001))
#print(numbers)
print(max(numbers))
print(min((numbers)))
print(sum((numbers)))

#odd numbers
odd_numbers=list(range(1,21,2))
for number in odd_numbers:
    print(number)

#Threes
multiples=list(range(3,31,3))
for value in multiples:
    print (value)

#Cubes
cubes=[value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)
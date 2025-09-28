#reading an entire file:
with open('pi_digits.txt') as obj:
    contents=obj.read()
print(contents.rstrip())

#reading a file line by line:
with open('pi_digits.txt') as obj:
    for line in obj:
        print(line.rstrip())

#reading a file line by line:
with open('pi_digits.txt') as obj:
    lines=obj.readlines()

for line in lines:
    print(line.rstrip())
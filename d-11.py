#try-except block:
try:
    print(5/0)
except ZeroDivisionError:
    print("number cant be divisible by zero")

#try-except-else block:
print('Enter any two number we will divide it')
print('Press q to exit the program anytime')

while True:
    num_1=input('Enter the first number:')
    if num_1=='q':
        break
    num_1=int(num_1)
    num_2=input('Enter the second number:')
    if num_2=='q':
        break
    num_2=int(num_2)

    try:
        answer=num_1/num_2
    except ZeroDivisionError:
        print('You cant divide by zero!')
    else:
        print(answer)

#Handling file not found error:
file_name='alice.txt'

try:
    with open(file_name, encoding='utf-8') as f:
        message=f.read()
except FileNotFoundError:
    print('File doesnot exist.')
else:
    print(message)
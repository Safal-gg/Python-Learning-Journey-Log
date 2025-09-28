#Addition:
while True:
    try:
        num_1=input('Enter first number:')
        num_2=input('Enter second number:')
        sum=int(num_1)+int(num_2)
    except ValueError:
        print('invalid input')
    else: 
        print(sum)
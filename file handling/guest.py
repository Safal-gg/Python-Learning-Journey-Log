#Guest:
with open('guest.txt','w') as file_object:
    name=input('Enter your name:')
    file_object.write(name)

#Guest book:
with open('guest_book.txt','w') as file_object:
    while True:
        print('Press Q to quit the program')
        name=input('Enter your name:')
        if name=='Q' or name=='q':
            break
        else:
            file_object.write(f"{name.title()} \n")

#Programming poll:
file_name='responses.txt'
with open(file_name,'a') as file_object:
    while True:
        print('Press Q to quit the poll')
        message=input('Why do you like program?')
        if message=='Q' or message=='q':
            break
        else:
            file_object.write(f"{message} \n")

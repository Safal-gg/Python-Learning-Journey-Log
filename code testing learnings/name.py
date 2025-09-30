from name_function import get_formatted_name

print('enter q to exit the program anytime.')

while True:
    firstname=input('Enter your first name:')
    if firstname=='q':
        break
    lastname=input('Enter your last name:')
    if lastname=='q':
        break
    fullname=get_formatted_name(firstname,lastname)
    print(fullname)

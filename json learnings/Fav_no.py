import json

try:
    with open('fav_no.json','r') as f:
        number=json.load(f)
except FileNotFoundError:
    number=input("enter your favorite number:")
    with open('fav_no.json','w') as f:
        json.dump(number,f)
        print(f'We will remember your number which is {number}')
else:
    print(f'Your favorite number is {number}')
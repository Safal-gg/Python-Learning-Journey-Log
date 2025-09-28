import json

username=input('Enter your name:')

with open('username.json','w') as f:
    json.dump(username,f)
    print(f'We will remember you {username.title()}')
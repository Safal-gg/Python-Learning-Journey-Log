import json

with open('username.json','r') as f:
    username=json.load(f)
    print(f'Hello! {username.title()}')
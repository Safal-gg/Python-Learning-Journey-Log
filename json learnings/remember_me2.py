import json

def get_username():
    try:
        with open('username_2.json') as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def ask_username():
    username=input('What is your name?')
    with open('username_2.json','w') as f:
        json.dump(username,f)
        return username
        
def greet_user():
    username=get_username()
    if username:
        print(f"Welcome back! {username.title()}")
        verify=input('Is this your username?(Y/N)')
        if verify=='Y':
            print(f"Welcome back! again")
        else:
            username=ask_username()
            print(f"Welcome back! {username.title()}")
        
    else:
        username=ask_username()
        print(f"We will remember you next time {username.title()}")

greet_user()
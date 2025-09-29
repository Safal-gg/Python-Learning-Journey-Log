#looping through a dictionary

users={
    'first name':'bob',
    'last name':'marley',
    'age':48
}

for key,value in users.items():
    print(f"\n Key:{key}")
    print(f"\n Value:{value}")

#nesting
#dictionary in a list
alien_0={'color':'green','points':'5','speed':'slow'}
alien_1={'color':'green','points':'5','speed':'slow'}
alien_2={'color':'green','points':'5','speed':'slow'}
aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

#making a list of 30 aliens and printing 5 of them
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:5]:
    print(alien)

#changing three aliens:
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['points']=15
        alien['speed']='fast'

for alien in aliens[0:5]:
    print(alien)

#list in dictionary:
pizza={
    'size':15,
    'toppings':['pepporoni','pineapple','cheese']
}

print("size of pizza you order is",pizza['size'])
print("toppings you ordered are:")

for topping in pizza['toppings']:
    print(f"\n {topping}")

#dictionary inside dictionary
users={
    'a':{
        'first_name':'lebron',
        'last_name':'james',
        'location':'LA'
    },
    'b':{
        'first_name':'john',
        'last_name':'stockton',
        'location':'Utah'
    }
}

for username,userinfo in users.items():
    print("\n Username:",username)
    print("First name:",userinfo['first_name'])
    print("Last name:",userinfo['last_name'])
    print("location:",userinfo['location'])

#user input
age=input('enter your age')
age=int(age)
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
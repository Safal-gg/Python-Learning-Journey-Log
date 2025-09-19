#people:
person_1={
    'first_name':'sam',
    'last_name':'altman',
    'age':26,
    'city':'san fransisco'
}
person_2={
    'first_name':'mark',
    'last_name':'zuck',
    'age':33,
    'city':'LA'
}
person_3={
    'first_name':'hari',
    'last_name':'prasad',
    'age':18,
    'city':'moscow'
}
persons=[person_1,person_2,person_3]

for person in persons:
    print(f"First name is {person['first_name'].title()}")
    print(f"Last name is {person['last_name'].title()}")
    print(f"Age is {person['age']}")
    print(f"City is {person['city'].title()}")

#favorite places:

favorite_place={
    'levy':['italy','japan','russia'],
    'henry':['hawai','norway'],
    'james':['canada','spain','france']
}

for key,value in favorite_place.items():
    print(f"name:{key}")
    for place in value:
        print(f"{place}")

#cities
cities={
    'tokyo':{
        'country':'japan',
        'population':'41000000'
    },
    'chicago':{
        'country':'usa',
        'population':'2700000'
    },
    'moscow':{
        'country':'russia',
        'population':'13260000'
    }
}

for name,info in cities.items():
    print(f"City name:{name.title()}")
    print(f"Country it is situated in:{info['country'].title()}")
    print(f"Populationi:{info['population']}")

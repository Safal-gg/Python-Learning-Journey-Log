#Person:
person={
    'first_name':'sam',
    'last_name':'altman',
    'age':18,
    'city':'san fransisco'
}
print(person)

#Glossary:
Glossary={
    'list':'A order collection of items',
    'slice':'A part of list',
    'tuple':'An immutable list',
    'dictionary':'A collection of key value pairs'
}

for key,value in Glossary.items():
    print(f"{key.title()}:{value.title()}")




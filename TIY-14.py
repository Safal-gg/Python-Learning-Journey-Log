#Deli:
sandwich_orders=['cheese','mushroom','fish']
finished_sandwiches=[]

while sandwich_orders:
    finished_sandwich=sandwich_orders.pop()

    print(f"I made your {finished_sandwich.title()} sandwhich")

    finished_sandwiches.append(finished_sandwich)

print("Finished sandwhich are:")
for sandwhich in finished_sandwiches:
    print(sandwhich)

#No Pastrami:
new_sandwhiches=['cheese','pastrami','mushroom','fish','pastrami','pastrami']
print(new_sandwhiches)
print("The deli has run out of pastrami sandwhiches")

while 'pastrami' in new_sandwhiches:
    new_sandwhiches.remove('pastrami')

print(new_sandwhiches)

#Dream Vacation:
Vacations={}

poll_active=True

while poll_active:
    name=input("enter your name")
    vacation=input("enter your dream vacation")
    Vacations[name]=vacation
    ans=input("do you want to continue yes or no?")
    if ans.lower()=='no':
        poll_active=False

print("Poll result")
for name,vacation in Vacations.items():
    print(f"{name.title()} likes to go to {vacation.title()}")

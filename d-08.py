#Positional arguments:
def display_pets(pet_type,pet_name):
    print(f"My {pet_type.title()} is {pet_name.title()}")

display_pets('hamster','harry')

#Keyword arguments:
display_pets(pet_name='harry',pet_type='hamster')

#Default arguments:
def display_dogs(dog_name,dog_type='golden retriver'):
    print(f"My {dog_type.title()} name is {dog_name}")

display_dogs('rocky')

#Return value:
def full_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()

message=full_name('levy','rozman')
print(message)

#optional argument:
def full_name_formating(first_name,last_name,middle_name=""):
    if middle_name:
        print(f"{first_name} {middle_name} {last_name}")
    else:
        print(f"{first_name} {last_name}")

full_name_formating(first_name='Ram',last_name='Prasad')
full_name_formating(first_name='Ram',middle_name='Chandra',last_name='Prasad')

#Returning a dictionary
def display_info(first_name,favorite_food):
    info={'Name':first_name,
          'Food':favorite_food
          }
    return info

value=display_info('Bobby','Taco')
print(value)

#passing a list
def greet_users(names):
    for name in names:
        print(f"Hello! {name.title()}")

usernames=['amy','avin','abiral']
greet_users(usernames)

#Modifying list in function
unfinished_designs=['phone case','rubix cube','lamp model']
completed_designs=[]

def printing_models(unfinished,finished):
    while unfinished:
        finish=unfinished.pop()
        print(f"Printing: {finish.title()}")
        finished.append(finish)

def display_models(finished):
    for finish in finished:
        print(f"Finished models are :{finish.title()}")

printing_models(unfinished_designs[:],completed_designs)
display_models(completed_designs)

#Arbitary arguments:
def pizza(*toppings):
    for topping in toppings:
        print(topping)

pizza('pepporoni','cheese')
pizza('mushroom')

#mixing arbitary and positional arguments
def make_pizza(size, *toppings): 
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:") 
    for topping in toppings: 
        print(f"- {topping}") 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#using arbitary keyword argument
def getuser_data(first,last,**user_info):
    user_info['First name']=first
    user_info['Last name']=last
    return user_info

data=getuser_data('Hari','Prasad',location='kathmandu',height='55 inch')
print(data)
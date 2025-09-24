#slices
names=['hari','safal','vision','ronish','onyx']
print("First three items in the list are",names[:3])
print("Three items from the middle of the lists are:",names[1:4])
print("Last three items in the list are",names[-3:])

#my piizas, your pizzas
pizzas=['margherita','cheese','mushroom']

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print("\nI really like pizzas!")

friend_pizzas=pizzas[:]
friend_pizzas.append('pepporoni')
print(friend_pizzas)
print(pizzas)
import json

filename='numbers.json'

with open(filename,'r') as f:
    numbers=json.load(f)
    print(numbers)
import json
numbers=[1,2,3,4,5]

filename='numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)
with open('pi_digits.txt') as obj:
    lines=obj.readlines()

pi_string=''
for line in lines:
    pi_string+=line.strip()

print(pi_string)
print(len(pi_string))
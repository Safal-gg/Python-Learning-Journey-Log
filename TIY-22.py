from random import randint
from random import choice

class Dice:
    def __init__(self,sides=6):
        self.sides=sides

    def roll_dice(self):
        print(randint(1,self.sides))

my_dice=Dice(10)
my_dice.roll_dice()

#Lottery:
lottery_list = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
winners=[]
i=0
while i<4:
    ch=choice(lottery_list)
    winners.append(ch)
    i+=1

print(winners)

        
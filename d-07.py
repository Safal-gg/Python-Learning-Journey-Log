#while loops
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

#letting the user when to quit
message=""
while message!="quit":
    message=input("Tell me something I will " \
"repeat it back it to you and type quit if you want to exit the program")
    if message!='quit':
        print(message)

#using flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

flag=True
message=""
while flag:
    message=input(prompt)

    if message=="quit":
        flag=False
    else:
        print("message")
   
#printing odd numbers from 1 to 10:
current_number=0
while current_number<=10:
    current_number+=1
    if current_number%2==0:
        continue
    else:
        print(current_number)
    
#turning unverified users into verified users:
unverfied_users=['vartika','meenu','uday']
verified_users=[]
while unverfied_users:
    verified_user=unverfied_users.pop()
    print(f"Verifying user:{verified_user}")
    verified_users.append(verified_user)

print("The list of verified users are:")
for verified_user in verified_users:
    print(verified_user)

#removing instances:
pets=['dogs','fish','parrot','cat','iguana','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)

#polling:
response={}
poll_active=True

while poll_active!=False:
    name=input("enter your name")
    answer=input("which mountain would you like to climb")
    response[name]=answer

    repeat=input("would you like to continue yes/no?")
    if repeat.lower()=='no':
        poll_active=False


print("----poll result----")
for name,answer in response.items():
    print(f"{name.title()} likes to climb {answer.title()}")

#Defining a function:
def display():
    print("Hello")

display()

#Passing information through a function:
def display_message(message):
    print(f"Hello! {message.title()}")

display_message("How are you?")

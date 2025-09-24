names=['jared','luke','manny','george','safal']
if names:
 for name in names:
    if 'safal' in name:
        print(f"Hey admin, do you want the status report")
    
    else:
        print(f"{name.title()}, thanks for logging in again")

else:
   print("we need to find more users!")

#checking usernames
current_users=['Jared','luke','manny','george','safal']
new_users=['JARED','emily','levy','vision']

current_users_lower=[user.lower() for user in current_users]

for new_user in new_users:
   if new_user.lower() in current_users_lower:
      print("Sorry, you need to enter new username")
   else:
      print("Your name is available")

#ordinal numbers
numbers=[1,2,3,4,5,6,7,8,9]

for number in numbers:
   if number == 1:
      print(f"{number}st")
   elif number == 2:
      print(f"{number}nd")
   elif number == 3:
      print(f"{number}rd")
   else:
      print(f"{number}th")
        

Guests=['james','luke','amy']
print(f"{Guests[0].title()}, You have been invited to dinner!")
print(f"{Guests[1].title()}, You have been invited to dinner!")
print(f"{Guests[2].title()}, You have been invited to dinner!")

print(f"{Guests[0].title()} can't make it this time ;-;")
Guests[0]='bob'
print(f"{Guests[0].title()}, You have been invited to dinner!")
print(f"{Guests[1].title()}, You have been invited to dinner!")
print(f"{Guests[2].title()}, You have been invited to dinner!")

print("\n\n I have found a bigger table")

Guests.insert(0,'lara')
Guests.insert(2,'penny')
Guests.append('jimmy')
print(f"{Guests[0].title()}, You have been invited to dinner!")
print(f"{Guests[1].title()}, You have been invited to dinner!")
print(f"{Guests[2].title()}, You have been invited to dinner!")
print(f"{Guests[3].title()}, You have been invited to dinner!")
print(f"{Guests[4].title()}, You have been invited to dinner!")
print(f"{Guests[5].title()}, You have been invited to dinner!")

print("\n The big table won't arrive on time")
guest_1=Guests.pop()
print(f"{guest_1.title()}, Sorry you are not invited to the dinner")
guest_2=Guests.pop()
print(f"{guest_2.title()}, Sorry you are not invited to the dinner")
guest_3=Guests.pop()
print(f"{guest_3.title()}, Sorry you are not invited to the dinner")
guest_4=Guests.pop()
print(f"{guest_4.title()}, Sorry you are not invited to the dinner")

print(Guests)
print(f"{Guests[0].title()}, You are still on the list!")
print(f"{Guests[1].title()}, You are still on the list!")
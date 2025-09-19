#river
river={
    'nile':'egypt',
    'bagmati':'nepal',
    'amazon':'brazil'
}

for key,value in river.items():
    print(f"{key.title()} is in {value.title()}")

for key in river.keys():
    print(key)

for value in river.values():
    print(value)

#poll
favorite_languages={
    'jen':'ruby',
    'lenny':'c++',
    'henry':'python',
    'levy':'python'

}

poll_names=['jen','lenny']

for name in favorite_languages.keys():
    if name in poll_names:
        print(f"thank you for voting in the poll, {name}")
    else:
        print(f"{name} pls vote in the poll")
    

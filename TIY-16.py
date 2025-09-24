#T-Shirt:
def make_shirt(shirt_size='l',shirt_graphics='I love python'):
    print(f"The size of the shirt is:{shirt_size.upper()} & The message written in the shirt is: {shirt_graphics.title()}")

make_shirt('XL','addidas')
make_shirt(shirt_graphics='nike',shirt_size='L')
make_shirt()

#Cities:
def describe_city(city_name='Kathmandu',city_country='Nepal'):
    print(f"{city_name} is in {city_country}")

describe_city()
describe_city(city_name='Delhi',city_country='India')
describe_city(city_name='Moscow',city_country='Russia')

#Album:
def make_album(artist_name,album_title,no_songs=None):
    if no_songs:
        albums={'Name':artist_name,'Album name':album_title,'Number of songs':no_songs}
        return albums
    else:
        albums={'Name':artist_name,'Album name':album_title}
        return albums
    

value_1=make_album(artist_name='Ed Sheeran',album_title='minus',no_songs=13)
value_2=make_album(artist_name='Ed Sheeran',album_title='minus')
print(value_1)
print(value_2)

#Users Album:
while True:
    print('Enter your favorite album infos')
    print('\n you can quit any time by pressing q')
    artist=input("Enter artist name:")
    if artist=='q':
        break

    album=input("Enter album name")
    if album=='q':
        break

    songs=input("enter the number of songs")
    if songs=='q':
        break
    songs=int(songs)
    value=make_album(artist,album,songs)
    print(value)


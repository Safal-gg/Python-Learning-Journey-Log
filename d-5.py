#dictionaries
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_coordinates']=0
alien_0['y_coordinates']=25

print(alien_0)

#starting with empty dictionaries
alien_1={}
alien_1['color']='red'
alien_1['points']=10

print(alien_1)

#modifying values in a dictionary 
alien_2={'color':'green','points':5}
print("the alien color is:",alien_2['color'])

alien_2['color']='blue'
print("the alien color now is:",alien_2['color'])

#removing key value pairs

del alien_0['points']
print(alien_0)

#a dictionary with similar objects

favorite_languages={
    'jen':'ruby',
    'lenny':'c++',
    'henry':'python'
}
print(favorite_languages['jen'])

#using get() to access values 
alien_3={'points':5}
point_value=alien_3.get('color','no color attribute given')
print(point_value)
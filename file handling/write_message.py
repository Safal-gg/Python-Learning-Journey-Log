#Write mode:
with open('programming.txt','w') as file_object:
    file_object.write('Hello world \n')
    file_object.write('File is opened!! \n')
#Append mode:
with open('programming.txt','a') as file_object:
    file_object.write('And I am writing in the file')
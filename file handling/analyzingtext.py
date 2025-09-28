
def count_words(filename):
    try:
        with open(filename,'r') as file_obj:
            contents=file_obj.read()
    except FileNotFoundError:
        print('file doesnot exist')
    else:
        listofcontents=contents.split()
        print(listofcontents)
        length=len(listofcontents)
        print(f"the file has {length} number of words.")

count_words('guest.txt')
count_words('guest_book.txt')
count_words('pi_digits.txt')
count_words('line.txt')
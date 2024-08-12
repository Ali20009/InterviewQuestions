import os
source = 'C:\\Users\\Omid\\programming\\python\\WorkingwithFILES\\folder'
destination = 'C:\\Users\\Omid\\Desktop\\folder'  # to find location  go to  files  ->Desktop -> right click -> proerties ->Location

try:
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print(source +'was moved')
except FileNotFoundError:
    print(source + ' was not found ')
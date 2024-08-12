try:
    with open('C:\\Users\\Omid\programming\\python\\WorkingwithFILES\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('File was not found')

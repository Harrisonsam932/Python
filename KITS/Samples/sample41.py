
try:
    name = input("Enter a string pretty please: ")
    print(len(name))
except TypeError:
    print('Unable to find length of a dummy value')

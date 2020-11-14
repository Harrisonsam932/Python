
def display(arg):
    print('Hello')
    arg()
    
def display1():
    print('Hai')
    
var = display1
display(var)
    
    
    
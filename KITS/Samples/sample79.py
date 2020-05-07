
def display():
    print('hello')
    
    def display1():
        print('Hai')
        
    var = display1
    return var


var1 = display()
var1()
    
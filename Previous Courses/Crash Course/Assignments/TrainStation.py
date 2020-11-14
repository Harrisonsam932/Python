

#Train Booking/Reservation System
print ("""
Welcome to our Train Booking Site""")


#Global Variables:
seatcount = 72
station = {101: 'chennai', 102: 'delhi', 103: 'mumbai'}
price = ('1200 INR', '600 INR', '1500 INR')


def book():
    start = input("Where are you starting from? ")
    end = input("Where is your destination city? ")

    if start == station[101]:
        print(4)
        


def View():
    start = input("Where are you starting from? ")
    end = input("Where is your destination city? ")
    
    if start == station[101] and end == station[102] or start == station[102] and end == station[101]:
        print('Your trip will cost '+price[0])
        
    if start == station[101] and end == station[103] or start == station[103] and end == station[101]:
        print('Your trip will cost '+price[1])

    if start == station[102] and end == station[103] or start == station[103] and end == station[102]:
        print('Your trip will cost '+price[2])
        
    else:
        print('''The only available cities right now are: ''', 
              station)

book()
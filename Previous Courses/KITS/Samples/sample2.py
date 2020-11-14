
def convert(f):
    f = (temp*1.8)+32
    print(f)


temp = int(input("What is the temperature in Celsius?"))


decision = input("Would you like that in Fahrenheit?")

if decision == "yes":
    convert(temp)

else:
    print(temp)

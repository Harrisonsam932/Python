



def reverse(li):
    for each in li:
        for c in reversed(each):
            if c.isalpha(): 
                print(c, end="")
            else:
                print()
                break
    
fruits = ['ap!ple','bana@na','ma%ngo','#orange','pine*apple']
reverse(fruits)
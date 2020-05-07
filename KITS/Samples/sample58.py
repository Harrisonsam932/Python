
class Sample:
    
    li = []
    
    def __countVowel(self):
        opt = 'yes'
        while opt == 'yes':
            name = input('Character please...')
            if name in ('a','e','i','o','u'):
                self.li.append(name)
            opt = input('Do u want to continue:')
        return len(self.li)
    
    def get(self):
        res = self.__countVowel()
        print(res)
    


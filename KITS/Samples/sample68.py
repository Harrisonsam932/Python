
class A:

    def countVowel(self,name):
        c = 0
        for ch in name:
            if ch in ('a','e','i','o','u'):
                c+=1
        return c

class B(A):

    def displayReverse(self,name):
        for ch in reversed(name):
            print(ch)


obj = B()
print(obj.countVowel('surya'))
obj.displayReverse('surya')

sno = []
sname = []
m1 = []
m2 = []
m3 = []

opt = 'yes'

while opt == 'yes':
    snum = (input('enter the student number:'))
    name = (str)(input('enter the student name:'))
    marks1 = (int)(input('enter the student marks:'))
    marks2 = (int)(input('enter the student marks:'))
    marks3 = (int)(input('enter the student marks:'))
   
    sno.append(snum)
    sname.append(name)
    m1.append(marks1)
    m2.append(marks2)
    m3.append(marks3)
    
    opt = input('Do u want to continue:')
    tot = 0
    
    for i in range(0,len(sno)):
        tot += m1[i]+m2[i]+m3[i]
        avg = tot/3
        if avg >= 60 and marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
            result = 'First Class'
        elif avg >= 50 and avg < 60 and marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
            result ='Second Class'
        elif avg >= 35 and avg < 50 and marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
            result ='Third Class'
        else:
            result ='Fail'
        
        print(sno[i],'---',sname[i],'---',m1[i],'---',m2[i],'---',m3[i],'---',tot,'---',avg,'---',result)
        
 
    
    

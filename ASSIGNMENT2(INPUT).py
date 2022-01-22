QUESTION1
print('lenght of string is' ,len(statement1))
print(statement1[::-1])

b=statement1[12:90]
print(b)
c=statement1.replace('a case sensitive','object oriented')
print(c)
d=statement1.count('a')
print(d)
e=statement1.replace(' ','')
print(e)

QUESTION2:
name="Armeen_Singh"
branch="ECE"
SID=21105002
CGPA=9.9
print("Hey,",name,"Here!")
print('my SID is',SID)
print('I am from',branch,'department and my CGPA is ',CGPA)

QUESTION3:


a=56
b=10
print('a&b=' ,a&b)
print('a|b=',a|b)
print('a^b=',a^b)
print('a<<2=',a<<2)
print('b<<4=',b<<4)
print('a>>2=',a>>2)
print('b>>4=',b>>4)


QUESTION4:
num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if(num1>num2 and num1>num3):
        print('first number is greatest')
elif(num2>num1 and num2>num3):
        print('second  number is greatest') 
else:
        print('third number is greatest')

QUESTION5:
a=input("enter your string")
if("name" in a):
         print("yes")
else:
         print("no")

QUETION6:
a=int(input("enter 1st side of triangle"))
b=int(input("enter 2nd side of triangle"))
c=int(input("enter 3rd side of triangle"))
if(a+b>c and b+c>a and c+a>b):
      print("yes")

else:
      print("no")
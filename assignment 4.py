ASSIGNMENT 4:
QUESTION 1:
n=int(input('enter number of disks'))
def solution(n,source,intermediate,end):
    if n==1:
        print("move disk %s from %s to %s"%(n,source,end))
    else:    
       solution(n-1,source,end,intermediate)
       print("move disk  %s from %s to %s"%(n,source,end))
       solution(n-1,intermediate,source,end)
source="source"
intermediate="intermediate"
end="end"
a=solution(n,source,intermediate,end)
print(a)

QUESTION 2:

num=int(input('enter row number upto which you want to print row'))
big_list=[]

if num==1:
    print("1")


elif num<=0:
    print('enter a valid number')

else:
    for i in range(num):
        little_list=[] 
        for j in range(i+1):
            if j==0 or j==i:
                little_list.append(1)
            else:
                little_list.append(big_list[i-1][j-1] + big_list[i-1][j])
        big_list.append(little_list)
print()

for i in range(num):
    for j in range(num-i-1):
        print(" ",end=" ")

    for j in range(i+1):
        print(big_list[i][j],end=" ")
    print()

print("RECURSION METHOD")
def triangle_row(spaces,num_list):
    n_list = []
    n_list.append(1)
    if len(num_list)>=2:
        for i in range(len(num_list)-1):
            n_list.append(num_list[i]+num_list[i+1])
    if len(num_list)>=1:
        n_list.append(1)
    
    print("{}".format(" ") *spaces,end='')
    for num in n_list:
        print("{}".format(num),end=" ")
    spaces-=1
    print()
    if spaces>=0:
        triangle_row(spaces,n_list)

    
    
rows = int(input("Enter number of rows: "))
num_list =[]
triangle_row(rows-1,num_list)

QUESTION3:

num1=int(input('enter the value of first number'))
num2=int(input('enter the value of first number'))
remainder=num1%num2
quotient=num1//num2
def ques3(num1,num2):
    if num2==0:
        print('division is not defined')
    else:
        print(f"remainder of division of two numbers entered is: {num1%num2} and quotient is : {num1//num2}")
    if num1==0 and num2==0 and num1%num2==0 and num1//num2==0:
      print('all values are zero')
    else:
      print('all values are not zero')#b

ques3(num1,num2)
print(callable(ques3))#a
sett=set()
for i in range(4,7):
    qwe=remainder+i#c
    rty=quotient+i
    if(qwe>4):
        sett.add(qwe)
        print(sett)
    if rty>4:
        sett.add(rty)
        print(sett)
print(sett)#d
set1=frozenset(sett)
print('the immutable set is:',set1)#e
print("largest value is ",max(set1))
qwerty=max(set1)#f
print("hash value is",hash(qwerty))#f

QUESTION4:

class Student:
    def __init__(self,name,roll_number):
       self.name=name
       self.roll_number=roll_number
    def __def__(self):
        print('destructor is here!!!')
s1=Student('Armeen Singh',1)
s2=Student('Qismat',2)
print(s1.name)
del s1

QUESTION5:

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
Mehak=Employee('Mehak',40000)
Ashok=Employee('Ashok',50000)
Viren=Employee('Viren',60000)
Mehak.salary=70000 #a
print(Mehak.salary)
del Viren.salary
print( Viren.salary)


QUESTION6:

george_word=input("Hey George enter the word")
lower_word=george_word.lower()
ready_string=[i for i in lower_word]
      
print(f"Dear Barbie your job is to make a new word from following words:{ready_string}")
barbie_word=input('enter your word Barbie')
lower1_word=barbie_word.lower()

ready_2string=[j for j in lower1_word]
if len(lower_word)==len(lower1_word):
    print(" I guess Barie is your true friend but not 100 percent ,working to find...")
else:
    print('OH!!!,Barbie and George you failed to prove your true friendship :(')

ready_string.sort()
ready_2string.sort()
def final_test():
      if ready_string==ready_2string:
                   print( "CONGRATS!!! you are TRUE frinds")
      else:
                   print('fake friendship :(')
      
print("BE PATIENT RESULT IS COMING :)")
final_test()
       
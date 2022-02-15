QUESTION 1:
string_name=str(input("Enter the string:"))
list1=string_name.split()
#empty list which will contain lowercase words only
list_l=[]

for e in list1:
    lower_e=e.lower()
    list_l.append(lower_e)
set1=set(list_l)
dic={}
#forming a dictionary with key string and value string count
for el in set1:
    count=list_l.count(el)
    dic.update({el:count})
#Code when string contains only one word
dic2={}       #empty dictionary
set2={1,2}
set2.clear()  #empty set2
list2=[]      #empty list2
#Condition when only one word is detected in string
if len(list1)==1:
    #Code for counting letter
    #Adding all letters of input string into  list2
    for elements in string_name:
        list2.append(elements)
    #lowering elements of list2 to lowercase and adding to set2
    for el in list2:
        set2.add(el.lower())
    #lowering main input string to lowercase
    string_l=string_name.lower()
    for elem in set2:
        #Adding count values to dic2
        dic2.update({elem:string_l.count(elem)})
    # printing the dic2 containing 'letter':'letter count'
    print("\nDictionary containing 'Letter':'Letter Count' is shown below:")
    print(dic2)
#printing the dic when string contains more than one word
else:
    print("\nDictionary containing {'Word':'Word Count'} is shown below:")
    print(dic)      #dic contains 'word':'word count'

QUESTION 2
q=[1,3,5,7,8,10]
w=[4,6,9,11]

year=int(input('enter the year'))
if year%4==0:
    print('LEAP YEAR')
    month=int(input('enter the ongoing month'))
    if month in q:
        date=int(input('enter the date'))
        if 0<date<=30:
            print('tomorrow is',date,'/',month,'/',year)
        elif date==31:
            print('tomorrow is 1/',month+1,'/',year)
    elif month in w:
        date=int(input('enter the date'))
        if 0<date<=29:
            print('tomorrow is',date,'/',month,'/',year)        
        elif date==30:
            print('tomorrow is 1/',month+1,'/',year)
    elif month==2:
        date=int(input('enter the date'))
        if 0<date<=28:
            print('tomorrow is',date,'/',month,'/',year)        
        elif date==29:
            print('tomorrow is 1/',month+1,'/',year)
    elif month==12:
        date=int(input('enter the date'))
        if 0<date<=30:
            print('tomorrow is',date,'/',month,'/',year)        
        elif date==31:
            print('tomorrow is 1/1','/',year+1)
    else:
        print('ENTER A VALID MONTH!!!')
else:
    print(' NOT A LEAP YEAR')
    month=int(input('enter the ongoing mpnth'))
    if month in q:
        date=int(input('enter the date'))
        if 0<date<=30:
            print('tomorrow is',date,'/',month,'/',year)
        elif date==31:
            print('tomorrow is 1/',month+1,'/',year)
    elif month in w:
        date=int(input('enter the date'))
        if 0<date<=29:
            print('tomorrow is',date,'/',month,'/',year)        
        elif date==30:
            print('tomorrow is 1/',month+1,'/',year)
    elif month==2:
        date=int(input('enter the date'))
        if 0<date<=27:
            print('tomorrow is',date,'/',month,'/',year)        
        elif date==28:
            print('tomorrow is 1/',month+1,'/',year)
    elif month==12:
        date=int(input('enter the date'))
        if 0<date<=30:
            print('tomorrow is',date,'/',month,'/',year)        
        elif date==31:
            print('tomorrow is 1/1','/',year+1)
    else:
        print('ENTER A VALID MONTH!!!')        

QUESTION 3:
numbers_input1=input('enter the numbers here')
list1=numbers_input1.split()
convert_to_integer=map(int,list1)
list2=list(convert_to_integer)
print(list2)
list3=[]
for i in list2:
    tuple1=(i,i**2)
    list3.append(tuple1)
print(list3)

QUESTION 4:
grade=int(input('please enter you grade '))
if grade ==4:
    print('your grade is ','D','your performance is poor!!! ')
elif grade ==5:
    print('your grade is ','C','your performance is below average!!! ')
elif grade ==6:
    print('your grade is ','C+','your performance is average!!! ')
elif grade ==7:
    print('your grade is ','B','your performance is good!!! ')
elif grade ==8:
    print('your grade is ','B+','your performance is very good!!! ')
elif grade ==9:
    print('your grade is ','A','your performance is excellent!!! ')
elif grade ==10:
    print('your grade is ','A+','your performance is outstanding(: ')
else:
    print('ERROR')

QUESTION 5:
n = 6

for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()

QUESTION 6
dict1={}
ques=input('do you want to enter more details?')
while ques=='y' or ques=='Y':
    name=input('enter the name')
    sid=int(input('enter the sid'))
    dict1.update({sid:name})
    ques=input('do you want to enter more details?')
    if ques=='Y' or ques=='y':
        continue
    else:
        break
while ques=='n' or ques=='N':
        print('HAVE A NICE DAY!!!')
        break
print(dict1)
list_k=sorted(dict1)
dict2={}
for ele in list_k:
    dict2.update({dict1.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dict2)
ort_dic = sorted(dict1)
dict3 = {}
for va in dict1:
    dict3.update({va: dict1.get(va)})
print("The Dictionary after sorting according to SID:")
print(dict3)
enter_sid = int(input("Enter SID to get name of student:"))
output_name = str(dict1.get(enter_sid))
print("Name of student with SID", {enter_name,'is',{output_name})

QUESTION 7
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))

if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")

else:
    #code for fibonacci series for first 2 elements
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        
        list1 = [1, 1]
    
        a = 1
        b = 1
        
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)

        sum = 0    #intial sum=0
        
        for num in list1:
            sum = sum + num
        average = (sum / n)
        
        two_decimal = "{:.2f}".format(average)
        
        print(f"\nAverage of given fibonacci series is {two_decimal}")


QUESTION 8
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
set4=set1^set2
print(set4)
set5=set1^set2|set2^set3|set3^set1
print(set5)
set6=set1&set2|set2&set3|set3&set1
print(set6)
set7=set()
for  i in range(1,11):
 if i not in set1: 
   set7.add(i)
print(set7)
set8=set()
for i in range(1,11):
    if i not in set1 and i not in set2 and i not in set3:
        set8.add(i)
print(set8)

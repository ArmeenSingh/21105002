Program 1:
a=int(input('enter your number'))
b=int(input('enter your number'))
c=int(input('enter your number'))
avg=(a+b+c)/3
print('average of numbers is ',avg)

Program 2:
income=int(input('enter your income'))
dependents=int(input('enter number of dependents'))
taxable_income=income-10000-(3000*dependents)
tax=taxable_income*0.2
print('taxable income:',taxable_income )
print('tax=',tax)

Program 3:
sid=input('enter your SID')
name=input('enter your name')
gender=input('what is your gender')
course_name=input('enter your branch')
CGPA=float(input('enter your CGPA'))
student=[sid,name,gender,course_name,CGPA]
print(student)


Program 4:
marks_student1=int(input('enter marks of student1'))
marks_student2=int(input('enter marks of student2'))
marks_student3=int(input('enter marks of student3'))
marks_student4=int(input('enter marks of student4'))
marks_student5=int(input('enter marks of student5'))
list=[marks_student1, marks_student2, marks_student3, marks_student4, marks_student5]
list.sort()
print('list of students',list)

Program 5:
color=['red','green','white','black','pink','yellow']
color.pop(3)
print(color)
color[2]='purple';color[3]='purple'
print(color)

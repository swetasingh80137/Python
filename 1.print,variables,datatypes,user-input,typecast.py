print ('hii')
print("world")
print("this is my first program")
print("""world
this is my first python program
i hope you all like it""")
print("world \nthis is my first python program")
print("world \nthis is my first python program \ni hope you all like it")
#in this program I have written hello world and does the print statement part
"""hello 
this is comment 
added by me """

a="hello"
print(a)
#RULES OF WRITING VARIABLES- Name,name ;EvenNum, Even_Num; Num1, special characters
Name="john"
print(Name)
EvenNum=2
print(EvenNum)
Num1=25
print(Num1)

#USER INPUT---- string(default), integer(int), floating points(float- decimal), evaluate(eval)
name=input("enter your name here")
print(name)
age= int(input("enter your age here"))
length=float(input("enter length of the rectangle"))
print(length)
exp1= eval(input("enter any equation here"))
print(exp1)

#typecasting and subtypes
name="john"
print(type(name))
a=123
b=1.23
print(type(a))
print(type(b))
c=a+b
print(c)
print(type(c))
a=145
b=32.62
c=a+b
print(c)

a="123"
b=1.23
a= int(a)
print("after conversion",type(a))

#write a program to display a person's name, age and address in three diff line
name= "john"
age=23
address= "654 lake street"
print(name)
print(age)
print(address)

#write a program to swap two variables
#method1
x=12
y=13
temp=x
print(temp)
x=y
print(x)
y=temp
print(y)

print ("value of x is",x)
print("value of y is",y)

#method2- left, right= right, left
a=30
b=40
a,b=b,a
print("value of a is",a)
print("value of b is",b)

#write a program to convert a float into integer
a=1.23
a=int(a)
print("after coversion",type(a))
print(a)

#write a program to take details from a student for ID card and then print in differnt lines

name= input ("enter name of student")
grade= input("enter grade of the student")
age= int(input("enter age of student"))
email= input("enter email of student")
ph_no= input("enter phone number")
print("student identity card")
print("name:", name)
print("grade:", grade)
print("age:", age)
print("email id:", email)
print("phone no.:", ph_no)

#write a program to take an user input as integer then convert it to float
x=1
print(type(x))
x= float(x)
print("value of x is",x)
print(type(x))







#LISTS ARE COLLECTION OF ORDERED AND MUTABLE DATA
#MUTABLE-ONCE CREATED, CAN BE CHANGED
#WRITTEN INSIDE SQUARED BRACKETS
#VALUE SEPERATED BY COMMA
#MULTIPLE DATATYPES CAN BE WRITTEN INSIDE A LIST

fruits= ["apple", "mango", "banana", 12, 14, 1.25]
print(fruits)
print (type(fruits))


print("-"*1200)
#LIST SLICING
a= ["ironman", "thor","hulk","captain america"] #[0,1,2,3] #[-4,-3,-2,-1]]
print(a[2])
print (a[-3])
print (a[1:3]) #[ starting value: ENDING value+1]
print(a [ :2]) #not defining starting i.e. by default 0
print(a [1:]) #not define ending that is by default the end of list
print(a[::2]) #[starting value: ending value: GAP+1]
print(a[-3:-1]) #negative values
print(a[::-1]) #REVERSE the list
print(a[-1:-4:-1]) #reverse within a range [starting: ending: reverse]

#============================================================================================================
#LIST ITERATION

print("-"*1200)
#ITERATION USING FOR LOOP ------------
a= ["ironman", "thor","hulk","captain america"]
for i in a :
    print(i)

print("-"*1200)
#ITERATION USING FOR LOOP WITH RANGE AND LENGTH FUNCTION
for i in range (len(a)):
    print(i)
for i in range (len(a)):
    print(a[i])

print("-"*1200)
#ITERATION USING WHILE LOOP
i=0
while i< len(a):
    print(a[i])
    i +=1

print("-"*1200)
#ITERATION USING SHORT-HAND FOR LOOP
[print(i) for i in a]


#===================================================================================================================
print("-"*1200)


a= ["ironman", "thor","hulk","captain america"]

#LENGTH OF LIST
print(len(a))

#COUNT OCCURENCE OF PARTICULAR ELEMENT
print(a.count("hulk"))

#ADD ELEMENT TO LIST --- at the end of list
a.append("spiderman")
print(a)

#ADD ELEMENT TO SPECIFIC LOCATION
a.insert(1,"vision")  #index no. , replacement word
print(a)

#TO REMOVE FROM A LIST
a.remove("hulk")
print(a)

#TO REMOVE FROM A CERTAIN LOCATION
print(a.pop(1))


#TO CREATE A COPY OF LIST
a= ["ironman", "thor","hulk","captain america"]
b= a.copy()
print(b)


#TO ACCESS AN ELEMENT
print(a.index("ironman"))

#TO EXTEND THE LIST
c= ["vision","mission"]
a.extend(c)
print(a)

#TO REVERSE THE LIST
a.reverse()
print(a)

#TO SORT THE LIST
a.sort()
print(a)

d=[1,7,6545,5,6,8,215]
d.sort()
print(d)


#TO CLEAR ALL THE DATA FROM THE LIST
a.clear()
print(a)

#==================================================================================================================
print("-"*1200)
#LIST COMPREHENSION

l1=[30,40,50,60]
l2=[]
for i in l1:
    l2.append(i)
print(l1, "\n", l2)   #\n--- to change line

for i in l1:
    if i>45:
        l2.append(i)
print(l1, "\n",l2)


l3= [i for i in l1] ######list comprehension
print(l3)

l3= [i for i in l1 if i>45]
print(l3)


#=============================================================================================================
print("-"*1200)

A= ["ross", "rachel", "monica", "joe"]   #INDEX[0,1,2,3]

#WRITE A PROGRAM TO SWAP FIRST AND FOURTH ELEMENT
A[0], A[3] =A[3], A[0]
print(A)


#WRITE A PROGRAM TO ADD A NEW VALUE AT SECOND POSITION
A.insert(1,"phoebe")
print(A)

#WRITE A PROGRAM TO DELETE A VALUE FROM 3RD POSITION
A.pop(2)
print(A)

#WRITE A PROGRAM TO MULTIPLY ALL THE NUMBERS IN THE LIST
B=[13,7,12,10]
multiply= 1
for i in (B):
    multiply *= i
print(multiply)


#WRITE A PROGRAM TO GET LARGEST AND SMALLEST NUMBER FROM THE LIST
B=[13,7,12,10]
B.sort()   #arrange in ascending order
print(B)
print(B[-1]) #LARGEST VALUE IS THE LAST NO. that is -1
print(B[0])  #smallest value is the first value is 0


#


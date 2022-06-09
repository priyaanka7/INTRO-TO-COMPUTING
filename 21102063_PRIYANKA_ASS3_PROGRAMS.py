#Program for Question 1
print("Question 1")
a=50
convert = bin(a)
print(convert)
print("\n")


#Program for Question 2
print("Question 2")
a= str(input('Enter expression:'))
print("Ans:", eval(a))
print("\n")


#Program for Question 3
print("Question 3")
import math
print("Q3(a)")
a=(3+4)*5
print("(3+4)*5=", a)

print("Q3(b)")
n= int(input("Enter value of n:"))
b=n*(n-1)/2
print("n*(n-1)/2=",b)

print("Q3(c)")
r= int(input("Enter value of r:"))
c=4*(math.pi)*r**2
print("value:",c)

print("Q3(d)")
r= int(input("Enter value of r:"))
a= int(input("Enter value of a:"))
b= int(input("Enter value of b:"))
c=math.sqrt(r*(math.cos(a))**2+r*(math.sin(b))**2)
print("Value:",c)

print("Q3(e)")
y1= int(input("Enter value of y1:",))
y2= int(input("Enter value of y2:",))
x1= int(input("Enter value of x1:",))
x2= int(input("Enter value of x2:",))
a=(y2-y1)/(x2-x1)
print("(y2-y1)/(x2-x1):",a)
print("\n")


#Program for Question 4
print("Question4")
print("Q4(a)")
print("Numbers generated for range(5):")
for i in range(5):
    print (i)

print("Q4(b)")
print("Numbers generated for range(3,10):")
for i in range (3,10):
    print(i)

print("Q4(c)")
print("Numbers generated for range(4,13,3):")
for i in range (4,13,3):
    print(i)

print("Q4(d):")
print("Numbers generated for range(15,5,-2):")
for i in range (15,5,-2):
    print(i)

print("Q4(e):")
print("Numbers generated for range(5,3):")
for i in range(5,3):
    print(i)
print("\n")


#Program for Question 5
H=eval(input("How many hydrogen atoms?"))
C=eval(input("How many carbon atoms?"))
O=eval(input("How many oxygen atoms?"))
Total=(H*1.00794)+(C*12.0107)+(O*15.9994)
print("The total molecular weight is:", Total)








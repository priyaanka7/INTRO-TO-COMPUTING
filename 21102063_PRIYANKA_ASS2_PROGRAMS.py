#Program for Question 1
print("Question 1")
input_string="Python is a case sensitive language"
print(input_string)
#Q1a)
print("\nPart a")
print("Length of the string is", len(input_string))
#Q1b)
print("\nPart b")
print("The string in reverse order is:", input_string[::-1])
#Q1c)
print("\nPart c")
new_string=input_string[10:27]
print(new_string)
#Q1d)
print("\nPart d")
part_1=input_string.replace("a case sensitive", "object oriented")
print("After replacing in input string:", part_1)
#or was confused that in which one string we have to replace so replacing in both
part_2=new_string.replace("a case sensitive", "object oriented")
print("After replacing in new string created in part c:", part_2)
#Q1e)
print("\nPart e")
print(input_string.index("a"))
#Q1f)
print("\nPart f")
print(input_string.replace(" ",""))
#End of program 1
print("\n")

#Program for Question 2
print("Question 2")
Name="Hey, {name} here!".format(name="Priyanka")
SID="My SID is {sid}".format(sid=21102063)
intro="I am from {dept} department and my CGPA is {cgpa}".format(dept="Civil", cgpa=float(10))
print(Name)
print(SID)
print(intro)
#End of program 2
print("\n")

#Program for Question 3
print("Question 3")
a=56
b=10
print("a=", a)
print("b=", b)
print("\nPart a")
print("a&b:", a&b)
print("\nPart b")
print("a|b:", a|b)
print("\nPart c")
print("a^b:", a^b)
print("\nPart d")
print("Left shifting both a and b with 2 bits:", a<<2, b<<2)
print("\nPart e")
print("Right shifting a with 2 bits and b with 4 bits:", a>>2, b>>4)
#End of program 3
print("\n")

#Program for Question 4
print("Question 4")
enter_string=str(input("Enter a string:"))
if("name" in enter_string):
    print("Yes")
else:
    print("No")
#End of program 4
print("\n")

#Program for Question 5
print("Question 5")
side1=input("Enter first side length:")
side2=input("Enter second side length:")
side3=input("Enter third side length:")
side1=int(side1)
side2=int(side2)
side3=int(side3)
if(side1==0 or side2==0 or side3==0):
#As none of the side of a triangle can be zero so, it will not form a trianlge
    print("No")
elif(side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
#As the sum of any two sides is greater than the third side, it will form a triangle
    print("Yes")
else:
#As the sum of any two sides is not greater than the third side, it will not form a triangle
    print("No")
#End of program 5
print("\n")

#Program for Question 6
print("Question 6")
flips = 0
a = int(input( "Enter the number ="))
b =int (input( "Enter the number ="))
for x in range(a+b):
    t1=a&1
    t2 =b&1
    if (t1!=t2):
        flips+=1
        a>>=1
        b>>=1
print(flips)





#PROGRAM FOR Q1
print("Q1")
a = int (input(" Please Enter the First Number: "))
b = int (input(" Please Enter the Second Number: "))
c = int (input(" Please Enter the Third Number: "))
average=(a+b+c)/3
print("The average of three numbers is ",average)
#End of program 1
print("\n")


#PROGRAM FOR Q2
print("Q2")
Tax_Rate=0.20
Gross_Income= int(input("enter your income:") )
Standard_deduction = 10000
No_of_dependents= int (input(" Enter number of dependents:"))
Dependent_deduction= 3000
Taxable_Income = Gross_Income - Standard_deduction - (Dependent_deduction*No_of_dependents)
Tax= Taxable_Income*Tax_Rate
print("Tax:", Tax)
#End of program 2
print("\n")




#PROGRAM FORQ3
print("Q3")
SID=int (input("Enter SID:"))
Name= input("Enter Name:")
Gender= input("Enter Gender:")
Course_Name= input("Enter Course Name:")
CGPA=float(input("Enter CGPA:"))
Student=[SID,Name,Gender,Course_Name,CGPA]
print(Student)
#End of program 3
print("\n")




#PROGRAM FOR Q4
print("Q4")
Student1= int(input("Marks of First student:"))
Student2= int(input("Marks of Second student:"))
Student3= int(input("Marks of Third student:"))
Student4= int(input("Marks of Fourth student:"))
Student5= int(input("Marks of Fifth student:"))
Marks= [Student1, Student2, Student3, Student4, Student5]
print(Marks)
#End of program 4
print("\n")




#PROGRAM FOR Q5
print("Q5")
List =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
List.remove('Black')
print ("Q5A)Expected List:color", List)
List =List[ :List.remove('Pink')]+['Purple']
print("Q5B) Expected List:color",List)
#End of program 5


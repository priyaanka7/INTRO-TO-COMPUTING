#Program for Question 1
print("Question1")
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i
if (sum == n):
    print(" %d is a Perfect Number" %n)
else:
    print(" %d is not a Perfect Number" %n)
print("\n")



#Program for Question 2
print("Question2")
#A palindrome is a word, phrase, or sequence that reads the same backward as forward,e.g., madam or nurses run.
st1=input("Enter text:")
st2=st1[::-1]
if (st1==st2):
  print('palindrome')
else:
  print('not palindrome')
print("\n")



#Program for Question 3
#Pascal's Triangle:
from math import factorial
n = 5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()
print("\n")
 


#Program for Question 4
print("Question4")
def ispangram(str):
    alphabet = "abcdefghijlkmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        return True
string = 'the quick brown fox jumps over the lazy doggi'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")
print("\n")
 


#Program for Question 5
print("Question5")
items=[n for n in input("Enter: ").split('-')]
items.sort()
print('-'.join(items))
print("\n")
 


#Program for Question 6
print("Question6")
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name: {kwargs['student_name']}")
        print(f"Student Class: {kwargs['student_class']}")
student_data(student_id='21102063', student_name='Priyanka', student_class='Civil')
student_data(student_id='21102033', student_name='Chhavi', student_class ='Civil')

print("\n")
 


#Program for Question 7
print("Question7")
class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class :")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print("\n")
 


#Program for Question 8
print("Question8")
def findTriplets(arr, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
    if (found == False):
        print("does not exist")
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)
print("\n")
 


#Program for Question 9
print("Question9")
class validity:
    def f(str):
        a= ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str
s = input("enter : ")
print(s, "-", "is balanced"
if validity.f(s) else "is Unbalanced")

#Program for Question 1
print("Question1")
a=int(input("Enter Your Marks:"))
if a<25:
    print("Your Grade is F")
elif 25<a<45:
    print("Your Grade is E")
elif 45<a<50:
    print("Your Grade is D")
elif 50<a<60:
    print("Your Grade is C")
elif 60<a<80:
    print("Your Grade is B")
else :
    print("Your Grade is A")
print("\n")



#Program for Question 2
print("Question2")
year = int(input("Enter the year = "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(year,"is a Leap year")
        else:
            print(year,"is not a Leap year")
    else:
        print(year,"is a Leap year")
else:
    print(year,"is not a Leap year")
print("\n")



#Program for Question 3
print("Question3")
import random
print("10 random multiple questions")
n=0
for n in range (0,10):
    a=random.randint(1,30)
    b=random.randint(1,10)
    print("First number is:",a)
    print("First number is:",b)
    c=a*b
    d=int(input("Your answer is:"))
    if d==c:
          print("Your answer is right")
    else:
          print("Your answer is wrong \n The correct answer is:",c)
    n+=1
print("\n")



#Program for Question 4
print("Question4")
a=1
while a<200:
    if (a%5==2) and (a%6==3) and (a%7==2):
        print("The number of candies in a halloween bowl are:",a)
    a+=1

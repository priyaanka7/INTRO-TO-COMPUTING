#Program for Question 1
print("Question1")
a= input("Enter the statement: ")
b=a[::-1]
print(b)
print("\n")


#Program for Question 2
print("Question2")
a=int(input("Enter the number: "))
b=int(input("Enter the lower limit: "))
c=int(input("Enter the upper limit: "))
for i in range(b,c):
  if i%a==0:
    print(i)
print("\n")



#Program for Question 3
print("Question3")
a=eval(input("Enter the first side length: "))
b=eval(input("Enter the second side length: "))
c= eval(input("Enter the third side lenth : "))
s=(a+b+c)/2
area =(s*(s-a)*(s-b)*(s-c))**0.5
if (a+b)>c:
    if (b+c)>a:
        if(c+a)>b:
            print(area,"area")
else:
  print("no area")
print("\n")



#Program for Question 4
print("Question4")
n=5;
for i in range(n):
    for j in range(i):
        print ('* ',end=" " )
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ',end=" ")
    print('')
print("\n")



#Program for Question 5
print("Question5")
rows = int(input("Enter the number of rows: "))
print("Triangluar Pattern of alphabets: ")
alphabet = 65
for i in range(rows):
  for j in range(i + 1):
    print('%c' %alphabet, end = ' ')
    alphabet = alphabet + 1
  print()
print("\n")



#Program for Question 6
print("Question6")
lower_value = int(input ( "Enter the lowest Range value : " ))
upper_value = int(input ( "Enter the upper Range Value : "))
for number in range (lower_value, upper_value + 1 ):
  if number > 1 :
    for i in range (2, number):
      if (number % i)== 0:
        break
else:
  print (number)
print("\n")



#Program for Question 7
print("Question7")
nl=[]
for x in range(1,500):
   if (x%7==0) and (x%11==0):
     nl.append(str(x))
print (','.join(nl))
print("\n")



#Program for Question 8
print("Question8")
lst = []
for i in range(0, 10):
   ele = int(input(" Enter the numbers: "))
   lst.append(ele)
pn = []
nn = []
on = []
en = []
for i in range(0, 10):
  if(i>=0):
     pn.append(i)
  if(i<0):
     nn.append(i)
  if(i%2==0):
     on.append(i)
  if(i%2!=0):
     en.append(i)
print("Q8(a) Positive numbers: ")
print(pn)
print("Q8(b) Negative numbers: ")
print(nn)
print("Q8(c) Odd numbers: ")
print(on)
print("Q8(d) Even numbers: ")
print(en)
def word_count(lst):
   counts = dict()
   for word in lst:
     if word in counts:
        counts[word] += 1
     else:
        counts[word] = 1
   return counts
print("Q8(e) Number of times each number occurs in the List: ")
print( word_count(lst))
print("\n")



#Program for Question 9
print("Question9")
user_list = input("Enter the list of words: ")
word_list = user_list.split(",")
counts = dict()
for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)



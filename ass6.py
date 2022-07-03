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
def isPalindrome(x):
    return x == x[::-1]
x = input("enter a word: ")
y = isPalindrome(x)
if x:
    print("Yes")
else:
    print("No")
print("\n")



#Program for Question 3
print("Question3")

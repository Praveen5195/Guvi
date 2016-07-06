num = int(input("enter the number to check for palindrome:"))

rev = 0
temp = num


while temp!=0:
    rev = rev * 10
    rev = rev + temp%10
    temp = temp//10

if rev == num:
    print("the number is palindrome")
else:
    print ("number is not a palindrome")

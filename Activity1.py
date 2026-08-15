number = int(input("Enter the number : "))
original_num = number
reversed_num = 0
while number > 0 :
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10
if original_num == reversed_num:
    print("The number is palindrome :", reversed_num)
else:
    print("The number is not plaindrome :", reversed_num)

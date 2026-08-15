small_num = int(input("Enter the  small number : "))
large_num = int(input("Enter the  large number : "))

while(small_num):
    x = small_num
    small_num = large_num % small_num
    large_num = x
print("The HCF is : ", large_num)
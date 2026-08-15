small_num = int(input("Enter the small number : "))
large_num = int(input("Enter the large number : "))
a = small_num
b = large_num
while(small_num):
    x = small_num
    small_num = large_num % small_num
    large_num = x
HCF = large_num
lcm = (a*b) // HCF
print("The lcm is : ", lcm)
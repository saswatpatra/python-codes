# Enter a number to check whether it is Armstrong or not
# 153 = sum of the cube of its digits is the same number, so it is Armstrong

num = int(input("Enter a number\n"))
digit = 0
sum = 0
temp = num

while num > 0:
    digit = num % 10
    sum += (digit ** 3)
    num //= 10

if temp == sum: 
    print(temp, "is an Armstrong number")
else:
    print(temp, "is not an Armstrong number")

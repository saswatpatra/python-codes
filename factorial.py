# Enter a number and finds its factorial

num = int(input("Enter a positive number\n"))
temp = num
factorial = 1

if num<0:
  print("Factorial cannot be found")
else:
  while num>0:
    factorial = factorial*num
    num -= 1
  print("Factorial of",temp, "is", factorial)

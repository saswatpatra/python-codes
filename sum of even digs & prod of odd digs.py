# Enter a number and find the sum of its even digits and the product of its odd digits respectively

num = int(input("Enter a number:\n"))

sum = 0
product = 1
even_count = 0
odd_count = 0

while num>0:
  x = num%10
  if num%2==0:
    sum += x
    even_count += 1
  else:
    product *= x
    odd_count += 1
  num = num//10

if even_count > 0:
  print("Sum of even digits = ", sum)
else:
  print("No even digits found, so sum of even digits = ", sum)
if odd_count > 0:
  print("Product of odd digits = ", product)
else:
  print("No odd digits found, so product of odd digits = ", product)

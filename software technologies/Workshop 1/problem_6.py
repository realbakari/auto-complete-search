# Write a program which takes a number n and adds up the numbers in the
# range 0..n.

n = int(input("Input: "))
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)

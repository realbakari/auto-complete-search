# Given a number n, write while and for loops that add up the numbers in the
# series 1,2,3,4,..., n-2, n-1, n and display the resultant sum. The number n will be input by
# the user of the algorithm.


n = int(input())

sum = 0
for i in range(1,n+1):
    sum +=i
print(sum)
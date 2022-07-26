# Given three integers, a b c, one of them is small, one is medium and one is
# large. Print True if the three values are evenly spaced, so the difference between small
# and medium is the same as difference between medium and large. Otherwise, print
# False.

sorted_list = sorted(list(map(int, input("Input: ").split())))

def evenlySpaced(x):
    if x[1] - x[0] == x[2] - x[1]:
        return True
    else:
        return False

print(evenlySpaced(sorted_list))

# OR

a = int(input())
b = int(input())
c = int(input())

slit = sorted(a,b,c)
if slit[1] - slit[0] == slit[2] - slit[1]:
    print("True")
else:
    print("False")


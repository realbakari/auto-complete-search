# Input a list of integers, print True if 6 appears as either the first or last element
# in the list. The list will be length 1 or more.

def first_last6(nums):
    if nums[0] == 6 or nums[len(nums)-1] == 6:
        print("True")
    else:
        print("False")
first_last6([1, 2, 6])
first_last6([1,2,3])
first_last6([3,2,1])

# Second Solution
input_list = list(map(int, input("Input a list of numbers: ").split()))
print(input_list)

def find_true(x):
    for i in range(len(x)):  # check if first or last element in input_list and return true.
        if x[0] == 6 or x[-1] == 6:
            return True
    else:
        return False

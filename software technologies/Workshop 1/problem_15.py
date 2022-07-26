# Write a function that given a list length 1 or more of integers, print the
# difference between the largest and smallest values in the list.

input_list = list(map(int, input("Input: ").split()))  # Assign in a list as Ints and split them.

def val_difference(usr_input):
    usr_input.sort()  # Sort it so it's in ascending order to make it easier to grab elements
    output = usr_input[-1] - usr_input[0]  # The highest number take away the smallest = the difference

    return output


print(val_difference(input_list))

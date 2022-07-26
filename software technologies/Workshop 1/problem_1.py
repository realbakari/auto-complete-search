hours, minutes, seconds = map(int, input("Input: ").split())  # We need to have int values not strings, map it.
print("Output:",hours * 3600 + minutes * 60 + seconds)  # * by how many seconds in those values and print

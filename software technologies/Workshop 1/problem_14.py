# Write a program that reads the file phillip.txt, counts the number of words in
# the file, and prints out the count.

contents = open("phillip").read()  # Default read val
words = contents.split()

print("Number of words in selected text file =", len(words))

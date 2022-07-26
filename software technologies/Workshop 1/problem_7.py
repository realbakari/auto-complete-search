# Given 2 strings, a and b, print a new string made of the first char of a and the
# last char of b, so "yo" and "Python" yields "yn". If either string is length 0, use '@' for its
# missing char. For example:

a = input("First Input: ")
b = input("Second Input: ")

def Char_string(a, b):
    new_char_1 = a[-len(a)]
    new_char_2 = b[-1]
    return new_char_1 + new_char_2

print(Char_string(a, b))

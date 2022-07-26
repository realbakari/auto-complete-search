# Given 2 strings, a and b, print a string of the form short+long+short, with the
# shorter string on the outside and the longer string on the inside. The strings will not be
# the same length, but they may be empty (length 0).

def combo_string(a, b):
    if (len(a) < len(b)):
        return a + b + a
    return b + a + b

print(combo_string('Hello', 'hi'))  # 'hiHellohi'
print(combo_string('hi', 'Hello'))  # 'hiHellohi'
print(combo_string('aaa', 'b'))  # 'baaab'

# Given a string, print a version without the first 2 chars. Keep the first char if it is
# 'a' and keep the second char if it is 'b'. The string may be any length.

def de_front(str):
    s = ''

    if str[0] == 'a' and str[1] == 'b':
        s = str
    elif str[0] == 'a' and str[1] != 'b':
        s = str[0] + str[2:]
    elif str[0] != 'a' and str[1] == 'b':
        s = str[1:]
    else:
        s = str[2:]

    return s

print(de_front('Hello')) #llo
print(de_front('java')) #va
print(de_front('away')) #aay

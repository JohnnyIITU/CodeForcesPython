# UPPER 65-90
# LOWER 97-122
string = input()
isError = int('1')
for i in range(1, len(string)):
    if ord(string[i]) > int('96'):
        isError = int('0')
if isError == int('1'):
    if ord(string[0]) < int('91'):
        char = string[0]
        string = string.lower()
        string = chr(ord(char) + int('32')) + string[1:]
    else:
        char = string[0]
        string = string.lower()
        string = chr(ord(char) - int('32')) + string[1:]
print(string)

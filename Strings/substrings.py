alphabet = "ABCDEFGHIJKLM"
print(alphabet[0])
print(alphabet[3])
print(alphabet[-1])
print(alphabet[3:6])
print(alphabet[:6])
print(alphabet[6:])

#substring replacement
fullName = "Stanislav Petrov"
#The contents of `fullName` haven't changed
diffrentName = fullName.replace("Stan", "Bob")
print(diffrentName)
#overwrite the contents of `fullName`
fullName = fullName.replace("Stan", "Bob")
print(fullName)

#https://docs.python.org/3/library/string.html
#string operations

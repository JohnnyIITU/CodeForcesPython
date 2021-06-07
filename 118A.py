word = input().lower()
exceptt = ['a', 'o', 'y', 'e', 'u', 'i']
finalWord = ""
for character in word:
    if(character not in exceptt) :
        finalWord += ("."+character)
print(finalWord)

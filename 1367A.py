n = int(input())
words = []
for i in range(n) :
    words.append(input())
for word in words : 
    start = word[0]
    end = word[len(word)-int(1)]
    checkWord = word[int(1):len(word)-int(2)]
    result = start+checkWord[::2]+end
    print(result)
                
    

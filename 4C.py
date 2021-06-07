n = int(input())
usernames = []
Counts = dict()
for i in range(n) :
    usernames.append(input())
    Counts[usernames[i]] = int(0)
for username in usernames :
    if(Counts[username] == int(0)) :
        print('OK')
    else :
        print(username+str(Counts[username]))
    Counts[username]+=1

    

from collections import defaultdict
def checkMagazine(magazine, note):
    flag=0
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word]+=1

    for word in note:
        if dicty[word] == 0:
            flag=1
        dicty[word]-=1

    if flag == 1:
        print("No")
    else:
        print("Yes")


mag=['give', 'me', 'one', 'grand', 'today', 'night']
note=['give', 'one', 'grand', 'today']
checkMagazine(mag,note)
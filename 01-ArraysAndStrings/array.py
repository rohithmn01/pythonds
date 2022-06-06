# """
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# """

import string
dict1={}
lis=['1', '3', '1', '4', '1', '3', '2', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '7']
alpha = list(string.ascii_lowercase[:26])
word="zaba"
#r=[]

for i in range(len(alpha)): 
    try:
        dict1.update({alpha[i]:lis[i]})
    except IndexError as e:
        dict1.update({alpha[i]:'0'})

#print(dict1)
maxi=0
for i in word:
    if int(dict1[i]) > maxi:
        maxi=int(dict1[i])
    #r.append(dict1[i])

harshi=maxi*len(word)
print(harshi)
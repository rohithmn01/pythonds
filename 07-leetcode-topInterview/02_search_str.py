import enum


word = ["monitor","mount","mouse","mega"]
word.sort()
s = "mouse"
s_lis=[]
final_list=[]
for i in range(len(s)):
    s_lis.append(s[:i+1])

print(s_lis)

for i in s_lis:
    sub_list=[]
    for w in word:
        if w.startswith(i):
            sub_list.append(w)
        if len(sub_list) == 3:
            break
    if [w] not in final_list:
        final_list.append(sub_list)

print(final_list)



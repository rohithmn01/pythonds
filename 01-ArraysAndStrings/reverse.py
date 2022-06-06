a="how are you madam my dad and were looking for you"
lis = a.split()


def check_pali(st):
    sta = list(st)
    rs = []
    for i in range(len(sta)-1,-1,-1):
        rs.append(sta[i])
    fin = ''.join(rs)
    if st == fin:
        print(st)
        return True
    else:
        return False
count=0
for strg in a.split():
    bol = check_pali(strg)
    if bol:
        count = count + 1

print(f"Number of palindromes: {count}")


import re
def validatePalin(s):
    #alpha_num_str = ''.join(ch for ch in s if ch.isalnum())
    alpha_num_str = re.sub(r'[^a-zA-Z0-9]', '',s) #substitute all the string that matches a non-alphanumeric character by an empty character
    #print(alpha_num_str.lower())
    rev=[]
    for i in range(len(alpha_num_str)-1,-1,-1):
        rev.append(alpha_num_str[i])
    revers = ''.join(rev)
    #print(revers.lower())

    if alpha_num_str.lower() == revers.lower():
        return "true"
    else:
        return "false"


def upperToLower(s):
    result = ''
    for ch in s:
        if ord(ch) >= 65:
            result = result + chr(ord(ch) - 32)
    print(result)


upperToLower("roHith")


res = validatePalin("race a car")
print(res)
def encode(s):
    f = s[0]
    tmp = ''
    count=1
    for i in range(1, len(s)):
        if f ==s[i]:
            count +=1
        else:
            if count==1:
                count = ''
            tmp = '%s%s%s' %(tmp, count, f)
            f =s[i]
            count = 1
    if count == 1:
        count = ''
    tmp = '%s%s%s' % (tmp, count, f)
    return tmp


s = 'aabbbccccdbbbdddcnnnnmmmmh'
print(encode(s))
def addfrequencytocharacter(s):
    frequency=[0]*26
    n=lens(s)
    for i in range(n):
        frequency[ord(s[i])-ord('a')]+=1
    for i in range(n):
        add=frequency[ord(s[i])-ord('a')]%26
        if(ord(s[i])+add<=ord('z')):
            s[i]=chr(ord(s[i])+add)
        else:
            add=(ord(s[i])+add)-(ord('z'))
            s[i]=chr(ord('a')+add-1)
    print("".join(s))
if'__name__'=='--main--':
    str = "ghee"
    
    addfrequencytocharacter([i for i in str])

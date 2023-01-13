def shuffle (11,12):
    c=[]
    if len(11)!-0 and len(12)!=0:
        for i in range(min (len(11), len(12))):
            c.extend([11[i],12[i]])
        c.extend(11[i+1] or 12[i+1])
    else:
        c.extend(11[0:] or 12[0:])
    return (c)
print(shuffle([1,2,3,8], [9,14,5,6,7,3]))

def removechar(s,c):
    counts=s.count(c)
    s=list(s)
    while counts:
        s.remove(c)
        counts -=1
        s=''.joins(s)
    print(s)
if __name__=='__main__':
    s="hello world"
    remove char(s,'1')

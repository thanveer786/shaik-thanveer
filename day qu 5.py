def calc():
    a=int(input('enter the value'))
    b=int(input('enter the value'))
    c=int(input('enter the value'))
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    elif c==4:
        print(a/b)
    else:
        print('invalid choice')

calc()


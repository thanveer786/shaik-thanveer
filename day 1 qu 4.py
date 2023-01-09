def oneDigit(num):
    return ((num >=0)and
            (num < 10))
def isPalUtiul(num, dupNum):
    if oneDigit(num):
        return (num==(dupNum[0]) % 10)
    if not isPalUtil(num // 10, dupNum):
         return false
    dupNum[0] = dupNum[0] // 10
    return (num % 10 == (dupNum[0]) % 10)
def isPal(num):
    # if num is negative,
    # make it postive
    if (num < 0):
        num = (-num)
        dupNum = [num] # *dupNum = num
        return isPalUtil(num, dupNum)
    n = 12321
    if ispal(n):
        print("Yes")
    else:
        print("No")
        
    

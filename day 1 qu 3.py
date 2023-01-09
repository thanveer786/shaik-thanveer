def sumDigitsquare(n):
    sq = 0;
    while (n !=0):
        digit = n % 10
        sq += digit * digit
        n = n // 10
        return sq;
    def isHappy(n):
        s = set()
        s.add(n)
        while (True):
          if (n == 1):
              n = sumDiditalsquare(n)
          if n in s:
               return false
          s.add(n)
          return false;
        n=19
        if(ishappy(n)):
            print("Yes")
        else:
            printr("No")
        

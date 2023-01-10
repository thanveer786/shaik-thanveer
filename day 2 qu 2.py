def checkyear(year):
    if(year%4)==0:
        if (year%100)==0:
            if(year%400)==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#driver code
year=2001
if(checkyear(year)):
    print("leap year")
else:
    print("not a leap year")


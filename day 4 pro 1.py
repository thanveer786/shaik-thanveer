for fizzbuzz in range(1,100):

    #Number divisible by 15,(divisible
    #by both 3&5),print'fizz'
    #in place of the number
    if fizzbuzz%15 ==0:
        print("fizzbuzz")
        continue
    #number divisible by 3,print'fizz'
    #in place of the number
    elif fizzbuzz%3 ==0:
        print("fizz")
        continue

    #number divisible by 5,
    #print'buzz'in
    #place of the number
    elif fizzbuzz%5==0:
        print("buzz")
        continue
    #print numbers
    print(fizzbuzz)

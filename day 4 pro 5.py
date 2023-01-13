# Returns minimum number of jumps to reach arr[n-1]from arr[0]
def minjumps(arr,n):
    # The number of jumps needed to reach the starting index is 0
    if(n<=1):
        return 0

    # Return-1 if not possible to jump
    if (arr[0]==0):
        return-1

    #initialization
    #stores all time the maximal recharchable index in the array
    maxReach=arr[0]
    # stores the amount of steps we can still take
    step=arr[0]
    # stores the amount of jumps neccesary to reach that maximal reachable position
    jump=1

    #start traversing array

    for i in range(1,n):
        # check if we have reached the end of the array
        if (i==n-1):
            return jump

        #updating maxReach
        maxReach =max(maxReach,i+arr[i])

        #we use a step to get to the current index
        step-=1;

        # if no further steps left
        if (step==0):
            # we must have used a jump
            jump+=1

            # check if the curent index/position or lesser index
            # is the maximum reach point from the previous indexes
            if(i>=maxReach):
                return-1
            #re-initialize the steps to the amount
            #of steps to reach maxReach from position i.
            step=maxReach-i;
      return-1
    #Driver program to test above function
    arr=[1,3,5,8,9,2,6,8.9]

    size=len(arr)
    # calling the minjumps function
    print("minimum number of jumpss to reach end is%d"% minjumps(arr,size))

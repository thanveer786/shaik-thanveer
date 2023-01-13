class solution:
    def smallernumbersthancurrent(self,nums:list[int])->list[int]:
        result=[]
        for num in nums:
            count=0
            for comp in nums:
                if num>comp:
                    count+=1
            result.append(count)
        return result
ob=solution()
print(ob.smallernumbersthancurrent([6,5,4,8]))

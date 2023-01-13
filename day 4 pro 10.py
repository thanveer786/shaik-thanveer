from random import sample

#initialize list
test_list=['python','programs','are','very','difficult']

#printing original list
print("the original list:"+str(test_list))

#scramble strings in list
#using list comphrension +sample()+join()
res=[''.join(sample(ele,len(ele))) for ele in test_list]

#printing result
print("scrambled strings in lists are:"+str(res))

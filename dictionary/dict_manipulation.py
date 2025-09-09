dict1 = {1:2,5:7}
dict2 = {9:3 , 8:9}
dict3 = {6:2, 5:2}

merge_dict = {}
result = {}

for d in [dict1,dict2,dict3] :
    for key ,value in d.items():
        merge_dict[key] = value

##print(merge_dict)

for d in [dict1,dict2,dict3] :
    result.update(d)

##print("concatenate value",result)

#write a python script to check whether the given dictionary is already exist in a dictionary.

dict4 = {1:2,4:5,7:8,9:10}

num = int(input())

if num in dict4:
    print("yes") 
else :
    print("No")



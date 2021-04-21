list=[2,2,6,5,4,5,61,5,61,4]
unique_list=[]
print(list)
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
input = open("Day6_input.txt", "r")


my_list=[]

document=[]
for line in input:   
    if line == "\n":
        my_list.append(document)
        document=[]
    else:
        temp=line.strip("\n").split(" ")
        document.extend(temp)
my_list.append(document)

#print(my_list)

list_dict=[]
for group in my_list:
    group_dic={}
    for passenger in group:
        for answer in passenger:
            if answer in group_dic.keys():
                group_dic[answer] = group_dic[answer] + 1
            else:
                group_dic[answer] = 1
    list_dict.append(group_dic)
    

#print(list_dict)

anyone_sum=0
for group_dic in list_dict:
    anyone_sum += len(group_dic.keys())
print(anyone_sum)



everyone_sum=0
for i,group_dic in enumerate(list_dict):
    num_people=len(my_list[i])
    for key in group_dic:
        if group_dic[key] == num_people:
            everyone_sum += 1
print(everyone_sum)
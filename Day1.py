
input = open("Day1_input.txt", "r")

my_list=[]
for line in input:
    my_list.append(int(line.strip("\n")))


for i in my_list:
    for j in my_list:
        if i+j == 2020 and i != j:
            multiplication2 = i*j
            break

print(multiplication2)


for i in my_list:
    for j in my_list:
        for k in my_list:
            if i+j+k == 2020 and i != j and i != k and j !=k :
                multiplication3 = i*j*k
                break

print(multiplication3)




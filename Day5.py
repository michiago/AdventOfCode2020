input = open("Day5_input.txt", "r")

my_list=[]
for line in input:
    my_list.append(line.strip("\n"))


seats=[]
for boarding_pass in my_list:
    position=[]
    begin_vertical=0
    end_vertical=127
    begin_oriz=0
    end_oriz=7
    for elem in boarding_pass:
        #print("begin: " + str(begin_vertical) + " end: " + str(end_vertical))
        if elem in ('B','F'):
            if elem == 'F':
                middle_vertical =(end_vertical-begin_vertical-1)/2
                end_vertical = end_vertical - middle_vertical -1
            elif elem == 'B':
                middle_vertical =(end_vertical-begin_vertical-1)/2
                begin_vertical = begin_vertical + middle_vertical +1
            if begin_vertical == end_vertical:
                position.append(begin_vertical)
        
        if elem in ('R','L'):
            if elem == 'R':
                middle_oriz=(end_oriz-begin_oriz-1)/2
                begin_oriz= begin_oriz + middle_oriz +1
            elif elem == 'L':
                middle_oriz=(end_oriz-begin_oriz-1)/2
                end_oriz=end_oriz - middle_oriz -1
            if begin_oriz == end_oriz:
                position.append(begin_oriz)
    
    id=position[0]*8+position[1]
    position.append(id)
    seats.append(position)

#print(seats)

# max_id=0
# for elem in seats:
#     if elem[2]>max_id:
#         max_id=elem[2]

# print(max_id)

id=[]
for elem in seats:
    id.append(elem[2])

print(max(id))

id.sort()

for i in range(len(id)):
    if i != len(id) -1:
        if id[i+1] != (id[i] +1):
            print(id[i])
            print(id[i+1])




            



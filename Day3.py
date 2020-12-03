import math 

input = open("Day3_input.txt", "r")
my_list=[]
for line in input:
    my_list.append(line.strip("\n"))
input.close()

def lineToKeep(i, line):
    if i == 1:
        return True
    elif i == 2:
        if line % 2 == 0:
            return True
        else:
            return False
    else:
        return False

TREES=[]
RIGHT = [1,3,5,7,1]
DOWN = [1,1,1,1,2]

for i, elem_right in enumerate(RIGHT):
    count_tree = 0
    position_in_line = 0
    num_line=0

       
    for line in my_list:
        if num_line != 0 and lineToKeep(DOWN[i], num_line) :
            num_line += 1
            if position_in_line + elem_right < len(line):
                position_in_line = position_in_line + elem_right
            else:
                position_in_line = elem_right - (len(line) - position_in_line) 
                    
            if line[position_in_line] == "#":
                count_tree += 1
        else:
            num_line +=1

    TREES.append(count_tree)

print(TREES)
print(math.prod(TREES))



#RIGHT 1 = 55
#RIGHT 3 = 250
#RIGHT 5 = 54
#RIGHT 7 = 55

#2, 7, 3, 4, 2
#43


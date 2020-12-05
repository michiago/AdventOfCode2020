input = open("Day4_input.txt", "r")

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



mandatory=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

num_doc_ok=0
for document in my_list:
    to_be_present=[0,0,0,0,0,0,0,0]
    for field in document:
        try:
            ind=mandatory.index(field[0:3])
            to_be_present[ind] += 1   
        except:
            pass
    
    if sum(to_be_present) == len(mandatory) or \
        ( sum(to_be_present) == (len(mandatory) -1) and \
            to_be_present[mandatory.index("cid")] == 0 ):
        num_doc_ok += 1


print(num_doc_ok)



input = open("Day2_input.txt", "r")

correct = 0
for line in input:
    temp = line.strip("\n").split()
    numbers=temp[0].split("-")

    min_occurrence = int(numbers[0])
    max_occurrence = int(numbers[1])
    letter = temp[1].strip(":")
    word = temp[2]

    cont = 0
    for elem in word:
        if elem == letter:
            cont += 1
    if (cont >= min_occurrence and cont <= max_occurrence):
        correct +=1

print(correct)
input.close()

input = open("Day2_input.txt", "r")

correct = 0
for line in input:
    temp = line.strip("\n").split()
    numbers=temp[0].split("-")

    first_position = int(numbers[0])
    second_position = int(numbers[1])
    letter = temp[1].strip(":")
    word = temp[2]

    if word[first_position -1] == letter and word[second_position -1] != letter or \
    word[first_position -1] != letter and word[second_position -1] == letter:
        correct +=1


print(correct)
input.close()


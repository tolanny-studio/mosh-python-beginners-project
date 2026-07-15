word_list = []
with open("./word.txt", "r") as file:
    for line in file:
        word_list.append(line.strip())
print(word_list)

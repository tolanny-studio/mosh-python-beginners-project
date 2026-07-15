import random

word_list = []
with open("word.txt", "r") as file:
    for line in file:
        word_list.append(line.strip())
print(word_list)

random_word = random.choice(word_list)
print(random_word)

blanks = ""

for _ in random_word:
    blanks += "_"

print(blanks)

guess = "a"

list_blanks = list(blanks)

print(list_blanks)

for index, char in enumerate(random_word):
    if char == guess:
        list_blanks[index] = guess


print(random_word)
print("".join(list_blanks))

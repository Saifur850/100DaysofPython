import random
word_list= ['saifur','tafsir','rakib']

# ran= random.randint(0,2)
# ran_word= word_list[ran]

ran_word= random.choice(word_list)

# print(ran_word)

word_list= []
for letter in ran_word:
    word_list.append(letter)
print(ran_word)
# print(word_list)

letter= input("Guess a letter: ")

for n in range(0,len(word_list)):
    if letter== word_list[n]:
        print("Right")
    else:
        print("Wrong")




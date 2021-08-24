import json
from os import truncate
import random

f = open('database.json')
data = json.load(f)
f.close()

vowels = "aeiou"
consonants = "bcdfgjklmnpqstvxzhrwy"
wordlist = []
chosen_names = []

iterations = input("Number of iterations: ")

while True:
    for i in range(int(iterations)):
        word = ""
        syl_len = random.randint(1,3)
        wordlist.append([])
        for x in range(syl_len):
            syl_let = random.randint(2,3)
            if syl_let == 2:
                if random.randint(1,2) == 1:
                    wordlist[i].append(random.choice(vowels) + random.choice(consonants))
                else:
                    wordlist[i].append(random.choice(consonants) + random.choice(vowels))
            if syl_let == 3:
                syl = ""
                if random.randint(1,2) == 1:
                    syl += random.choice(vowels)
                else:
                    syl += random.choice(consonants)

                if random.randint(1,2) == 1:
                    syl += random.choice(vowels)
                else:
                    syl += random.choice(consonants)

                if random.randint(1,2) == 1:
                    syl += random.choice(vowels)
                else:
                    syl += random.choice(consonants)
                wordlist[i].append(syl)
    i = 1
    for word in wordlist:
        temp = ""
        for syl in word:
            temp += syl
        print(temp + f" [{i}]")
        i += 1


    chosen_name = wordlist[int(input("Chosen name (number from top): ")) -1]
    chosen_names.append(chosen_name)
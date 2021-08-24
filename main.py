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

length_varying = 2

svq = 0
evq = 0
avg_len = 0

while True:
    iterations = input("Number of iterations: ")
    wordlist = []
    if chosen_names:
        end_l = []
        start_l = []
        end_vc = {
            "v":0,
            "c":0
        }
        start_vc = {
            "v":0,
            "c":0
        }
        lengths = []
        for n in chosen_names:
            name = ""
            l = 0
            for s in n:
                name += s
                l += 1
            lengths.append(l)
            end_l.append(name[-1])
            start_l.append(name[0])
            if name[-1] in vowels:
                end_vc["v"] += 1
            else:
                end_vc["c"] += 1
            if name[0] in vowels:
                start_vc["v"] += 1
            else:
                start_vc["c"] += 1
        svq = (start_vc['v'] / (start_vc['v'] + start_vc['c'])) * 100
        evq = (end_vc['v'] / (end_vc['v'] + end_vc['c'])) * 100
        avg_len = 0
        for l in lengths:
            avg_len += l
        avg_len /= len(chosen_names)
        print(f"Starting with a vowel: {svq}")
        print(f"Ending with a vowel: {evq}")
        print(f"Average length: {avg_len}")

    for i in range(int(iterations)):
        word = ""
        syl_len = random.randint(1,3)
        while (syl_len < avg_len - length_varying) or (syl_len > avg_len + length_varying):
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
                if x == 0 and svq != 0:
                    if random.randint(0,100) < svq:
                        syl += random.choice(vowels)
                    else:
                        syl += random.choice(consonants)
                else:
                    if random.randint(1,2) == 1:
                        syl += random.choice(vowels)
                    else:
                        syl += random.choice(consonants)

                if random.randint(1,2) == 1:
                    syl += random.choice(vowels)
                else:
                    syl += random.choice(consonants)
                if x == syl_len - 1 and evq != 0:
                    if random.randint(0,100) < evq:
                        syl += random.choice(vowels)
                    else:
                        syl += random.choice(consonants)
                else:
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
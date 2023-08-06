import random
import string


message = input("Enter message ")
words = message.split(" ")
coding = int(input("1 for Code and 0 Decode: "))

if coding == 1:
    new_words = []
    for word in words:
        if len(word) >= 3:
            r1 = random.choice(string.ascii_letters.lower())
            r2 = random.choice(string.ascii_letters.lower())
            for i in range(0, 2):
                r1 += random.choice(string.ascii_letters.lower())
                r2 += random.choice(string.ascii_letters.lower())
            new_string = r1 + word[1:] + word[0] + r2
            new_words.append(new_string)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))

else:
    new_words = []
    for word in words:
        if len(word) >= 3:
            a = word[-4]
            new_string = a + word[3:-4]
            new_words.append(new_string)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))

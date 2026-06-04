import random

toss = random.randint(1,10)

if toss % 2 == 1:
    print(toss)
    print("Heads!")
else:
    print(toss)
    print("Tails!")
import random

def sontop(x=10):
    rand_num = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    expectations = 0
    while True:
        expectations += 1
        guess = int(input(">>>"))
        if guess<rand_num:
            print(f"{guess}>>Dan Kattaroq son ayting:", end="")
        elif guess>rand_num:
            print(f"{guess}>>Dan Kichikroq son ayting:", end="")
        else:
            print("Yutdingiz!")
            break
        
    print(f"Tabriklayman. {expectations} ta taxmin bilan topdingiz!")
    return expectations

    
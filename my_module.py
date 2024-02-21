import random

def ass_val(name):
    call = toss()
    if name == "Head":
        name1 = 0
    else:
        name1 = 1
    won_or_loss(name1, call, name)

def toss():
    call = random.randint(0,1)
    return call

def won_or_loss(name1, call, name):
    if name1 == call:
        print(f"Your call is {name.title()} and you won the toss")
    else:
        print(f"Your call is {name.title()} and you lose the toss")
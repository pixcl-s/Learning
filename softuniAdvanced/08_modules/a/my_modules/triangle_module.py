def triangle(digit):
    thing = []
    for x in range(1, digit+1):
        thing.append(x)
        print(" ".join(str(y) for y in thing))
    for _ in range(len(thing)):
        thing.pop()
        print(" ".join(str(y) for y in thing))
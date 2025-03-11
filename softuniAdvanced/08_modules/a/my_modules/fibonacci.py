
def locate(list, num):
    if num == 1:
        print(f"The number - {num} is at index 1 and 2")
        return
    try:
        indeks = list.index(num)
    except ValueError:
        print(f"The number {num} is not in the sequence")
    else:
        print(f"The number - {num} is at index {indeks}")


def create(num):
    fibu = [0, 1]
    for x in range(1, num-1):
        fibu.append(fibu[-1] + fibu[-2])
    print(" ".join(str(x) for x in fibu))
    return fibu
def odd_sum_odd(a):
    i = 0
    while i < len(a) - 1:
        if a[i] % 2 != 0 and a[i + 1] % 2 != 0:
            a.insert(i + 1, a[i] + a[i + 1])
        i += 1
    return a

def find_index(a, ele):
    idx = []
    for i in range(len(a)):
        if a[i] == ele: idx.append(i)
    return a

def odd_even(a):
    for i in range(len(a)):
        if a[i] % 2 == 0 and a[i + 1] % 2 != 0:
            a[i], a[i + 1] = a[i + 1], a[i]
        if i == len(a) - 2:
            break
    return a

def draw_diamond(n):
    space = 2 * n - 2
    star = 1
    for i in range(1, n + 1):
        for j in range(space):
            print(" ", end = "")
        for j in range(star):
            print("* ", end = "")
        space -= 2
        star += 2
        print()
    space += 4
    star -= 4
    for i in range(n - 1, -1, -1):
        for j in range(space):
            print(" ", end = "")
        for j in range(star):
            print("* ", end = "")
        space += 2
        star -= 2
        print()


if __name__ == '__main__':
    draw_diamond(5)
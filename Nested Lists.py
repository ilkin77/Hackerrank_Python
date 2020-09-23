if __name__ == '__main__':

    arr = []
    score1 = []
    for x in range(int(input())):
        name = (input())
        score = float(input())
        arr.append([name, score])
        score1.append(score)

    c = min(score1)

    while min(score1) == c:
        score1.remove(min(score1))

    second = min(score1)

    for a, b in sorted(arr):
        if b == second:
            print(a)
if __name__ == '__main__':
    N = int(input())
    arr =[]
    for i in range(N):
        text = input()
        textSplit = text.split(" ")
        if textSplit[0] == 'insert':
            arr.insert(int(textSplit[1]), int(textSplit[2]))
        elif textSplit[0] == 'print':
            print(arr)
        elif textSplit[0] == 'remove':
            arr.remove(int(textSplit[1]))
        elif textSplit[0] == 'append':
            arr.append(int(textSplit[1]))
        elif textSplit[0] == 'sort':
            arr.sort()
        elif textSplit[0] == 'pop':
            arr.pop()
        elif textSplit[0] == 'reverse':
            arr.reverse()
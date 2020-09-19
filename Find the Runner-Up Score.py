if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    item=arr[0]
    for i in arr:
        if item != i:
            print(i)
            break
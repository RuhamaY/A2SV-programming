if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = max(arr)
    runner_up = -101  
    for score in arr:
        if score > runner_up and score < first:
            runner_up = score
    print(runner_up)

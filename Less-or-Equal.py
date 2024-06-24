def find_number(n, k, arr):
    arr.sort()
    if k == 0:
        if arr[0] > 1:
            return 1
        else:
            return -1
    if k == n:
        return arr[-1]
    if arr[k-1] < arr[k]:
        return arr[k-1]
    return -1

# Read input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Find and print the result
print(find_number(n, k, arr))

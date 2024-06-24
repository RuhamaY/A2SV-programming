def can_reduce_to_one_element(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return "NO"
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        results.append(can_reduce_to_one_element(arr))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

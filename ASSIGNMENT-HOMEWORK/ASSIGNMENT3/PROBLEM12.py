def get_min_diff(arr, k):
    n = len(arr)
    arr.sort()

    ans = arr[n - 1] - arr[0]
    smallest = arr[0] + k
    largest = arr[n - 1] - k

    for i in range(n - 1):
        mini = min(smallest, arr[i + 1] - k)
        maxi = max(largest, arr[i] + k)

        if mini < 0:
            continue

        ans = min(ans, maxi - mini)

    return ans


arr = [1, 5, 8, 10]
k = 2
print(get_min_diff(arr, k))

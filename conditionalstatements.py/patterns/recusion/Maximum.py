def maximum(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], maximum(arr, n - 1))

arr = [10, 25, 8, 50, 15]
print(maximum(arr, len(arr)))
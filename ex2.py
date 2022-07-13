def bigger_is_greater(w):
    arr = list(w)
    k = len(arr) - 1
    while k > 0 and arr[k - 1] >= arr[k]:
        k -= 1
    if k <= 0:
        return "no answer"

    j = len(arr) - 1
    while arr[j] <= arr[k - 1]:
        j -= 1
    arr[k - 1], arr[j] = arr[j], arr[k - 1]
    return "".join(arr)


for i in range(int(input())):
    print(bigger_is_greater(input()))

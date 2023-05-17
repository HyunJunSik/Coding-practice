arr = []
for i in range(int(input())):
    arr.append(list(map(int, input().split())))
def div(arr):
    length = len(arr)
    if length == 1:
        return str(arr[0][0])
    elif arr == [[0] * length for i in range(length)]:
        return str(arr[0][0])
    elif arr == [[1] * length for i in range(length)]:
        return str(arr[0][0])
    arr1 = [arr[i][:length//2] for i in range(length//2)]
    arr2 = [arr[i][length//2:] for i in range(length//2)]
    arr3 = [arr[i + length//2][:length//2] for i in range(length//2)]
    arr4 = [arr[i + length//2][length//2:] for i in range(length//2)]
    return div(arr1) + div(arr2) + div(arr3) + div(arr4)
result = div(arr)
print(result.count('0'), result.count('1'), sep='\n')
arr = [list(map(int, input().split())) for i in range(int(input()))]
def div(arr):
    length = len(arr)
    if length == 1:
        if arr[0][0] == -1:
            return '2'
        else:
            return str(arr[0][0])
    elif arr == [[0] * length for i in range(length)]:
        return str(arr[0][0])
    elif arr == [[1] * length for i in range(length)]:
        return str(arr[0][0])
    elif arr == [[-1] * length for i in range(length)]:
        return '2'
    new_arr = []
    for k in [0, length//3, length//3 * 2]:
        new_arr.append([arr[k + i][:length//3] for i in range(length//3)])
        new_arr.append([arr[k + i][length//3:length//3 * 2] for i in range(length//3)])
        new_arr.append([arr[k + i][length//3 * 2:] for i in range(length//3)])
    result = ''
    for arrs in new_arr:
        result += div(arrs)
    return result
result = div(arr)
print(result.count('2'), result.count('0'), result.count('1'), sep='\n')
        
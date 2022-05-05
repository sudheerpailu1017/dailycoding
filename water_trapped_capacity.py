'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

'''
def find_capacity(arr):
    if not arr:
        return 0

    result = 0
    max_i = arr.index(max(arr))

    lt = arr[0]
    for num in arr[1:max_i]:
        result += lt - num
        lt = max(lt, num)

    rt = arr[-1]
    for num in arr[-2:max_i:-1]:
        result += rt - num
        rt = max(rt, num)

    return result
    
arr=list(map(int,input().split()))
print(find_capacity(arr))
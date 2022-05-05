'''
Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
'''
def find_nonduplicated(arr):
    out_arr = [0] * 32
    for num in arr:
        for i in range(32):
            bit = num >> i & 1
            out_arr[i] = (out_arr[i] + bit) % 3

    out = 0
    for i, bit in enumerate(out_arr):
        if bit:
            out += 2 ** i

    return out
    
arr=list(map(int,input().split()))
print(find_nonduplicated(arr))
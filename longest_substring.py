'''Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"
'''

def longest_substring(s, k):
    curr= ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]
            if len(set(temp)) <= k and len(temp) > len(curr):
                curr= temp
    return len(curr)
    
s=input()
k=int(input())
print(longest_substring(s,k))
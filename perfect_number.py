'''A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28'''

def digits_sum(n):
    current_sum = 0
    while n > 0:
        current_sum += n % 10
        n = n // 10
    return current_sum

def find_perfect(n):
    i, current = 0, 0
    while current < n:
        i += 1
        if digits_sum(i) == 10:
            current += 1
    return i
    
n=int(input())
print(find_perfect(n))
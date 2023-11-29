import sys
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

def binary_search(array, target, left, right):
    if left > right:
        return False
    
    mid = (left + right) // 2
    middle = array[mid]
    if target == middle:
        return True
    elif target > middle:
        left = mid + 1
    else:
        right = mid - 1
        
    return binary_search(array, target, left, right)

    
m = int(input())
lst = list(map(int, input().split()))
for num in lst:
    if binary_search(A, num, 0, n-1):
        print(1)
    else:
        print(0)
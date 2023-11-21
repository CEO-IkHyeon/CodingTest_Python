import sys
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")

n, m = map(int, input().split())

lst = list(map(int, input().split()))

ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = lst[i] + lst[j] + lst[k]
            if tmp <= m:
                ans = max(ans, tmp)
                #print(lst[i], lst[j], lst[k], tmp)
print(ans)
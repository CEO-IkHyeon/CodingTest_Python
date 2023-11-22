import sys
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")

n, k = map(int, input().split())

ans = 1
for i in range(k):
    ans *= (n-i)

for i in range(k):
    ans /= (k-i)

print(int(ans))
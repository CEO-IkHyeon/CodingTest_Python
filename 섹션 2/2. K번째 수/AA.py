import sys
#sys.stdin = open(r"c:\Users\user\Desktop\CodingTest_Python\섹션 2\2. k번째 수\input.txt", "rt")

t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    num = sorted(num[s-1:e])

    print(f"#{i+1} {num[k-1]}")

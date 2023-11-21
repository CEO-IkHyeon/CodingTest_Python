import sys
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")

n = int(input())
lst = list(map(int, input().split()))

max_val = max(lst)

ans = (sum(lst) / max_val * 100) / n
print(ans)
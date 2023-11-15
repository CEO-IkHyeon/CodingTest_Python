import sys
#sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\섹션 2\5. 정다면체\input.txt", "rt")

n, m = map(int, input().split())

max_n = max(n,m)    

lst = [0 for _ in range(max_n * 2 + 1)]
# 굳이 max 값으로 lst 크기 세팅할 필요 X 
# n + m + 3 이면 충분

for i in range(1, n+1):
    for j in range(1, m+1):
        lst[i+j] += 1

max_val = max(lst)
for idx, num in enumerate(lst):
    if num == max_val:
        print(idx, end=" ")
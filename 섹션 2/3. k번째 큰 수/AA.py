import sys
#sys.stdin = open(r"c:\Users\user\Desktop\CodingTest_Python\섹션 2\3. k번째 큰 수\input.txt", "rt")
sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\섹션 2\3. k번째 큰 수\input.txt", "rt")

n, k = map(int, input().split())
lst = list(map(int, input().split()))

res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(lst[i]+lst[j]+lst[m])

res = list(res)
res.sort(reverse=True)

print(res[k-1])

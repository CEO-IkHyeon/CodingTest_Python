import sys
#sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\섹션 2\7. 소수(에라토스테네스 체)\input.txt", "rt")

n = int(input())

lst = [1 for _ in range(n+1)]

# 소수 : 2 -> 2의 배수 지우고 , 
for i in range(2, n+1):
    for j in range(i*2, n+1, i):
        lst[j] = 0

print(sum(lst)-2)
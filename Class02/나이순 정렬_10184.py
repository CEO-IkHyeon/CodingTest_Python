import sys
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(list(input().split()))

lst.sort(key=lambda x : int(x[0]))

for i in range(n):
    print(lst[i][0], lst[i][1])
    
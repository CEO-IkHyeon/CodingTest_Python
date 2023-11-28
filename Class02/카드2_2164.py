import sys
from collections import deque
sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\Class02\input.txt", "rt")

input = sys.stdin.readline

n = int(input())

lst = deque()
for i in range(1, n+1):
    lst.append(i)

while True:
    # lst의 원소가 1개인 경우
    if len(lst) == 1:
        print(lst[0])
        break

    lst.popleft()

    if len(lst) == 1:
        print(lst[0])
        break
    tmp = lst.popleft()
    lst.append(tmp)

    
    
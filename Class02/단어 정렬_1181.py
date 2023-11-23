import sys
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")

n = int(input())

set = set()
for _ in range(n):
    set.add(input())

lst = list(set)
lst.sort()
lst.sort(key=len)

for word in lst:
    print(word)
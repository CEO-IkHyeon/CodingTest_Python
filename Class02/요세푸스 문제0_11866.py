import sys
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [i for i in range(1, n+1)]

idx = 0
print("<", end='')
while lst:
    idx += k-1
    idx %= len(lst)
    tmp = lst.pop(idx)
    
    if len(lst) == 0:
        print(tmp, end ='')
    else:    
        print(tmp, end=', ')

print(">", end='')
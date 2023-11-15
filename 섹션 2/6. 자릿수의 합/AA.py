import sys
#sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\섹션 2\6. 자릿수의 합\input.txt", "rt")

def digit_sum(x):
    res = 0

    for i in str(x):
        res += int(i)

    # while x != 0:
    #     res += (x % 10)
    #     x = x // m
    
    return res

n = int(input())

lst = list(map(int, input().split()))

ans = 0
max_val = 0
for n in lst:
    tot = digit_sum(n)
    if  tot > max_val:
        max_val = tot
        ans = n


print(ans)
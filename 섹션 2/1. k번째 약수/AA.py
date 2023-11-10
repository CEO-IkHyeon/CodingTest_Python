import sys
#sys.stdin = open(r"c:\Users\user\Desktop\CodingTest_Python\섹션 2\1. k번째 약수\input.txt", "rt")

a, b = map(int, input().split())

divisor = []

for i in range(1, a+1):
    if a % i == 0:
        divisor.append(i)

if len(divisor) < b:
    print(-1)
else:
    print(divisor[b-1])

# cnt = 0
# for i in range(1, a+1):
#     if n%i==0:
#         cnt+=1
#     if cnt == b:
#         print(i)
#         break
# else:
#     print(-1)
    
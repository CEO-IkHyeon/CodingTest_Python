import sys


#sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\섹션 2\8. 뒤집은 소수\in2.txt", "rt")

def reverse(x):
    # ans = ""
    # for i in range(len(str(x))-1, -1, -1):
    #     ans += (str(x)[i])
    # return int(ans)

    ans = str(x)
    return int(ans[::-1])
    


def isPrime(x):
    if x == 1:
        return False
    
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True


n = int(input())

lst_num = list(map(int, input().split()))

for n in lst_num:
    tmp = reverse(n)
    if isPrime(tmp):
        print(tmp, end=" ")

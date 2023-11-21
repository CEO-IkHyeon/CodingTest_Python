import sys
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")

while True:
    n = int(input())
    if n == 0:
        break

    n = str(n)
    nLen = len(n)
    idx, flag = 0, 1

    while nLen//2 > 0:
        if n[idx] != n[len(n)-idx - 1]:
            flag = 0
        idx += 1
        nLen -= 1
    
    if flag:
        print("yes")
    else:
        print("no")
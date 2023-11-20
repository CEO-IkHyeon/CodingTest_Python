import sys
sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\Class02\input.txt", "rt")

while True:
    a, b, c = map(int, input().split()) 
    if a == 0:
        break
    max_val = max(a,b,c)
    flag = 0
    if a == max_val:
        if a**2 == b**2 + c**2:
            flag = 1
    elif b == max_val:
        if b**2 == a**2 + c**2:
            flag = 1
    elif c == max_val:
        if c**2 == a**2 + b**2:
            flag = 1

    if flag == 1:
        print("right")
    else:
        print("wrong")
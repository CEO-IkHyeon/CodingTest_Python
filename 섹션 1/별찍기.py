#피라미드 별 찍기

for i in range(10):
    for j in range(10, i, -1):
        print(" ", end='')
        
    for j in range(0, 2*i - 1):
        print("*", end='')

    print()

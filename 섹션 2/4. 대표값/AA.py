import sys
#sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\섹션 2\4. 대표값\input.txt", "rt")

n = int(input())

lst = list(map(int, input().split()))

avgScore = round(sum(lst) / n)

min_error = lst[0]
res = 0
score = 0 
for idx, num in enumerate(lst):
    tmp = abs(num-avgScore)

    if min_error > tmp:
        min_error = tmp
        score = num
        res = idx + 1
    elif tmp == min_error:
        if num > score:
            score = num
            res = idx + 1

print(avgScore, res)



    
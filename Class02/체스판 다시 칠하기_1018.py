import sys
sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\Class02\input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())

grid = []
checked = [[0 for _ in range(m)] for _ in range(n)]

# w로 시작 -> 짝수행,열은 W || 홀수행, 열은  B
# B로 시작 _
for i in range(n):
    grid.append(list(input().rstrip()))
  
print(grid)

 

#grid 돌면서 8x8 확인하기?

for i in range(n):
    for j in range(m):
        
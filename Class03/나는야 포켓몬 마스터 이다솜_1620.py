import sys
sys.stdin = open(r"C:\Users\IkHyeon\Desktop\CodingTest_Python\Class03\input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())

encyclopedia_int = dict()
encyclopedia_name = dict()
for i in range(1, n+1):
    name = input().strip()
    encyclopedia_int[i] = name
    encyclopedia_name[name] = i

for _ in range(m):
    problem = input().strip()
    if problem.isdigit():
        print(encyclopedia_int[int(problem)])
    else:
        print(encyclopedia_name[problem])  #index에서 O(n) 걸림 -> 여기서 시간 초과 발생하는 듯
        # 그럼 list를 사용하지말고 dictionary를 사용하자 읽을 때 시간 복잡도 O(1)임

        
# for e in encyclopedia:
#     print(e);
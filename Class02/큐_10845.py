# input 받을 때 웬만하면 "sys.stdin.readline().rstrip()"으로 받기
# 그래야 시간 초과 안남
# "rstrip()" 하는 이유는 readline()의 경우 우측에 자동으로 개행문자 들어감 -> 그거 없애려고

import sys
from collections import deque

sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\Class02\input.txt", "rt")

n = int(input())
q = deque()
lst = []
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    # print(command, len(command))

    if command == "front":
        # print("command FRONT execute")
        if len(q) == 0:
            lst.append(-1)
        else: 
            lst.append(q[0])

    elif command == "size":
        # print("command SIZE execute")
        lst.append(len(q))

    elif command == "empty":
        # print("command EMPTY execute")
        if len(q) == 0:
            lst.append(1)
        else:
            lst.append(0)

    elif command == "back":
        # print("command BACK execute")

        if len(q) == 0:
            lst.append(-1)
        else:
            lst.append(q[-1])

    elif command == "pop":
        # print("command POP execute")

        if len(q) == 0:
            lst.append(-1)
        else:
            lst.append(q.popleft())

    else:
        # print("command PUSH execute")
        cmd, num = command.split()
        q.append(num)

for num in lst:
    print(num)
import sys
sys.stdin = open(r"C:\Users\IkHyeon\Desktop\CodingTest_Python\Class03\input.txt", "rt")
input = sys.stdin.readline

m = int(input())

s = set()
for _ in range(m):
    cmds = input().split()

    cmd = cmds[0]
    if cmd == 'add':
        s.add(int(cmds[1]))
    elif cmd == 'remove':
        s.discard(int(cmds[1]))
    elif cmd == 'check':
        if int(cmds[1]) in s:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if int(cmds[1]) in s:
            s.discard(int(cmds[1]))
        else:
            s.add(int(cmds[1]))
    elif cmd == 'all':
        s = {i for i in range(1,21)}
    elif cmd == 'empty':
        s.clear()
    
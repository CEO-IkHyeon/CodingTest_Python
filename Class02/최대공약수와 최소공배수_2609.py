import sys
import math
sys.stdin = open(r"C:\Users\user\Desktop\CodingTest_Python\Class02\input.txt", "rt")

a, b = map(int, input().split())

print(math.gcd(a,b))
print(math.lcm(a,b))
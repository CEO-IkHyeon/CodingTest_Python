import sys

sys.stdin = open(r"C:\Users\andan\OneDrive\Desktop\PythonCoTe\CodingTest_Python\Class02\input.txt", "rt")

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

card_dict = dict()
for num in card:
    num = str(num)
    if num in card_dict:
        card_dict[num] += 1
    else:
        card_dict[num] = 1


m = int(input())
number = list(map(int, input().split()))

for num in number:
    num = str(num)
    if num in card_dict:
        print(card_dict[num], end=' ')
    else:
        print(0, end=' ')

# card.count(num) 으로 하면 매번 card list를 돈다 
# -> O(n) 소요 -> 이걸 m 번 진행 -> O(nm) 소요 될 것 -> 시간 초과
n = int(input())
sum = 0
list_n = []
for i in range(1, n+1):
    sum += i

    if n % i == 0:
        list_n.append(i)

    if i%2==0:
        continue
    print(i)

print("sum : ", sum)
print("n의 약수 : ", list_n)

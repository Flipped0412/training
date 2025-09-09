# for i in range(3, 0, -1):
#     print(i)

num_li = list(map(str, input().split()))
print(num_li)
a = ''.join(num_li)
print(a, type(a))
for i in a:
    print(i)

for i in range(len(a)):
    print(i)
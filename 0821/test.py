# arr = list(map(int, input().split()))
#
# print(arr.pop(0), arr)
# print(arr.pop(0), arr)
# print(arr.pop(0), arr)

nodes = [list(map(int, input().split())) for _ in range(5)]
print(nodes)
node_lst = []

for i in range(len(nodes)):
    for j in range(2):
        node_lst.append(nodes[i][j])

print(node_lst)
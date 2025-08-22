# def preorder_traerse(T):    # 전위 순휘
#     if T:                   # T is not None
#         visit(T)
#         preorder_traerse(T.left)
#         preorder_traerse(T.right)

# E, N = map(int, input().split())
# node_lst = list(map(int, input().split()))
# parents_lst = []
# childs_lst = []
#
# for i in range(0, E * 2, 2):
#     parents_lst.append(node_lst[i])
#
# for i in range(1, E * 2, 2):
#     childs_lst.append(node_lst[i])
#
# print(parents_lst)
# print(childs_lst)
#
# arr = [[0] * (5+1)] * 2
# print(arr)

E, N = map(int, input().split())
node_lst = list(map(int, input().split()))
arr = [[0] * (E + 1)] * 2
current = 0
check = 0

for i in range(0, E * 2, 2):
    if arr[0][node_lst[i - 1]] == 0:
        arr[0][node_lst[i - 1]] = node_lst[i + 1]
    else:
        arr[0][node_lst[i - 1]] = node_lst[i + 1]

while True:
    current = arr[0][current - 1]
    check += 1
    if current == 0:
        break
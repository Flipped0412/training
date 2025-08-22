# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13


# 중위순회
def inorder(v):
    if v == 0:
        return

    inorder(tree[v][0])
    print(v, end=' ')
    inorder(tree[v][i])


# 후위순회
def postorder(v):
    if v == 0:
        return

    postorder(tree[v][0])
    postorder(tree[v][i])
    print(v, end=' ')
    

V = int(input())
data = list(map(int, input().split()))
tree = [[0]*2 for _ in range(V+1)]
for i in range(0, (V-1)*2, 2):
    # data[i] : 부모 정점 번호
    # data[i+1] : 자식 정점 번호
    if tree[data[i]][0] == 0:  # 왼쪽 자식이 아직 없으면 왼쪽 자식에 저장
        tree[data[i]][0] = data[i + 1]
    else:
        tree[data[i]][1] = data[i + 1]  # 오른쪽 자식이 아직 없으면 오른쪽 자식에 저장

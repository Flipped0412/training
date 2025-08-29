# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def pre_order(T):
    if T > 0:
        print(T, end=' ')  # vistit(T)
        pre_order(left[T])  # pre_order(T.left)
        pre_order(right[T])  # pre_order(T.right)


def in_order(T):
    if T > 0:
        in_order(left[T])  # pre_order(T.left)
        print(T, end=' ')  # vistit(T)
        in_order(right[T])  # pre_order(T.right)

def post_order(T):
    if T > 0:
        post_order(left[T])  # pre_order(T.left)
        post_order(right[T])  # pre_order(T.right)
        print(T, end=' ')  # vistit(T)


V = int (input())
E = V - 1
arr = list(map(int,input().split()))

left = [0] * (V + 1)  # 부모 번호를 인덱스로 자식번호 저장
right = [0] * (V + 1)
par = [0] * (V + 1)  # 자식 번호를 인덱스로 부모번호 저장

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    par[c] = p
    left[p] = c

    # left 가 비어있으면 저장. 아니면 right 에 저장
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

print(left)
print(right)

root = 1
for i in range(1, V + 1):
    if par[i] == 0:  # 부모노드가 없는 경우
        root = i
        break

pre_order(root)
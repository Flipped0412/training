# 그래프 경로 복습
# V개 이내의 노드, E개의 간선
# 방향성 그래프
# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0 출력

def find_path(child):
    global flag

    if child == G:
        flag = 1
        return

    if arr[child] != 0:
        find_path(arr[child])
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    flag = 0
    map_list = [0]*(V + 1)

    for idx in arr:
        map_list[idx[0]] = idx[1]

    for child in arr[S]:
        find_path(child)

    print(f"#{tc} {flag}")
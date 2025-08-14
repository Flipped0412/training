def dfs():
    # 출발지는 0, 도착지는 99
    # 도착 가능하면1, 아니면 0 반환
    stack = [0]
    visited = [0]*100
    visited[0] = 1
    while stack:
        current = stack[-1]
        if current == 99:
            return 1
        # 현재 위치에서 갈 수 있는 길 가기
        for v in graph[current] :
            if v is not None and not visited[v]:
                stack.append(v)
                visited[v] = 1
                break
        else:
            stack.pop()


T = 10

for tc in range(1, T+1):
    tc, E = map(int, input().split())
    # 그래프 표시
    # 각 정점에서 갈 수 있는 길의 최대 개수가 2개
    # 각 정점마다 2개씩 갈 수 있는 정점 저장할 수 있도록 준비
    # 정점이 ㅗ치대 100개니까,, 2개짜리 100개 만들면 됩니다.
    graph = [[None]*2 for _ in range(100)]
    data = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        #  0번에 다른 숫자가 있으면 1번에 넣기 아니면 0번에 넣기
        if graph[data[i]][0] is None:
            graph[data[i]][0] = data[i + 1]
        else:
            graph[data[i]][1] = data[i + 1]

    result = dfs()
    print(f'#{tc} {result}')

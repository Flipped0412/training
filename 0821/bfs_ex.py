# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 그래프의 모양이 주어졌을 때 사용가능한 형태로 가공
# 사용할 수 있는 형태 : 인접행렬, 인접리스트 . . 등등
# v는 정점의 번호, 1번부터 v번까지
# E는 간선의 개수

V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
edges = list(map(int, input().split()))

for i in range(0, E * 2, 2):
    adj[edges[i]][edges[i+1]] = 1
    adj[edges[i+1]][edges[i]] = 1

for row in adj:
    print(row)


def bfs(start):
    # 시작점으로 부터 발견한 정점을 순서대로 탐색
    queue = [start]  # 리스트지만 pop(0) 과 append 만 활용하여 큐로 사용
    visited = [0] * (V+1)
    visited[start] = 1

    # 발견한 모든 정점을 탐색
    while queue:
        # current = stack[-1]   # DFS 기억해보기. 왔던 경로로 돌아가기 위해서 스택에 경로 저장
        # current = queue[0]    # 그래서 이런 다시 보기가 필요 없다
        current = queue.pop(0)  # 그말인즉 현재 정점에서 갈 수 있는 경로를 다 넣을 것이니, 냅다 빼버리면 된다
        print(current, end=' ')

        # 현재 정점에서 갈 수 있는 정점들 모두 확인해서 queue에 넣기
        for i in range(1, V+1):
            # current와 i번 정점이 연결되어 있고, i번 정점을 방문하지 않았으면,
            # i번 정점을 방문 할 것이라 남기기
            if adj[current][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1


bfs(1)

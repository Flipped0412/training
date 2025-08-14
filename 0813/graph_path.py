def dfs(S, G):
    stack = [S]
    visited = [0]*(V+1)
    visited[S] = 1

    while stack:
        current = stak[-1]

        if current == 6:
            return 1

        for v in adj[current]:
            if not visited[v]:
                stack.append(v)
                visited[v] = 1
                break
                # 반복문에서 break가 한 번도 안 걸림
        else:
            stack.pop()
    # 경로 찾기 반복문이 끝났는데 도착지에 도착하지 못했다? ==> 도착지로 가는 길이 없다
    return 0

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]

    for _ in range():
        pass
    
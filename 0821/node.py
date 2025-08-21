# 6 5
# 1 4
# 1 3
# 2 3
# 2 5
# 4 6
# [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]

def bfs(start):
    queue = [start]
    visitied = [0] * (V+1)
    visitied[start] = 1

    while queue:
        current = queue.pop(0)
        print(current, end=' ')

        for i in range(1, V+1):
            if adj[current][i] and not visitied[i]:
                queue.append(i)
                visitied[i] = 1

            if i == goal:
                break


t = int(input())

for tc in range(1, t+1):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    start, goal = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    node_lst = []

    for i in range(len(nodes)):
        for j in range(2):
            node_lst.append(nodes[i][j])

    for i in range(0, E*2, 2):
        adj[node_lst[i]][node_lst[i+1]] = 1
        adj[node_lst[i+1]][node_lst[i]] = 1

    bfs(start)

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    node_lst = list(map(int, input().split()))
    arr = [[0] * (E + 2) for _ in range(2)]
    current = N
    check = 0

    for i in range(0, E * 2, 2):
        if arr[0][node_lst[i]] == 0:
            arr[0][node_lst[i]] = node_lst[i + 1]
        else:
            arr[1][node_lst[i]] = node_lst[i + 1]

    while True:
        if current == 0 and arr[1][N] != 0:
            current = N

        if arr[0][current] == 0:
            tmp = current
            current = arr[1][current]
            arr[1][tmp] = 0
        else:
            tmp = current
            current = arr[0][current]
            arr[0][tmp] = 0

        if current == 0 and arr[0][N] == 0 and arr[1][N] == 0:
            break

        check += 1
        # print(check)

    print(f"#{tc} {check}")

    """
    1 2 3
    4 5 6
    7 8 9
    
    """
# arr = []
# for i in range(3):
#     arr.append(list(map(int, input().split())))
# arr = [list(map(int, input().split())) for _ in range(3)]
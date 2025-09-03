def find_apple():    # 사과를 찾으면 사과 번호와 좌표 저장
    for col in range(N):
        for row in range(N):
            if arr[row][col] != 0:
                apple_li.append([arr[row][col], col, row])


def find_next(col, row, i):  # 현재 사과에 대한 다음 사과의 4사분면 위치
    global sabun

    if i + 1 >= (len(apple_li)):  # 마지막 사과는 다음 사과가 없다
        return
    elif (apple_li[i+1][1] > col) and (apple_li[i+1][2] < row):  # 1사분면
        sabun = 1
    elif (apple_li[i+1][1] < col) and (apple_li[i+1][2] < row):  # 2사분면
        sabun = 2
    elif (apple_li[i+1][1] < col) and (apple_li[i+1][2] > row):  # 3사분면
        sabun = 3
    else:  # 4사분면
        sabun = 4


def cal_turn():
    pass


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    apple_li = []  # 사과 리스트에는 [[사과 번호, x좌표, y좌표], [사과 번호, x좌표, y좌표], , , ,] 이렇게 담긴다

    # 사과부터 찾자. 사과 리스트를 통해 사과가 몇개나 있는지도 알아낼 수 있다.
    find_apple()
    print(apple_li)  # [[3, 1, 3], [1, 2, 1], [2, 3, 2]]
    # 오름차순 정렬
    apple_li.sort()
    print(apple_li)
    # print(apple_li[0][1], apple_li[0][2])

    # 이제 현재 위치와 진행 방향에 비해 다음 사과의 위치가 몇사분면인지 구해보자
    sabun = 0
    for i in range(len(apple_li) - 1):
        find_next(apple_li[i][1], apple_li[i][2], i)
        apple_li[i+1].append(sabun)
    print(apple_li)

    # 4사분면을 찾았으니 이제 방향에 대해서 4사분면과 방향 그리고 회전수를 계산하자
    # 1번 사과를 먹었을 때는 항상 아래 방향으로 진행 중이며 1회전을 사용했다.
    # 그러므로 시작에서 1번 사과에 도달했다고 가정하고 2번사과부터 계산하자
    # 상하좌우 어디를 보고 있을 때 어느 4사분면에 있는지가 중요하기 때문에 상화좌우 방향도 정해준다.
    # 우 1, 하 2, 좌 3, 상 4 | 시작은 항상 아래를 보니 2로 시작한다.
    # cur_col = apple_li[0][1]
    # cur_row = apple_li[0][2]
    # cur_face = 2
    #
    # cal_turn(cur_col, cur_row, cur_face)
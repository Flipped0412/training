T = 10
for _ in range(T):
    tc = int(input())
    # 큐를 활용하기 위해 리스트의 pop(0) 와 append() 사용
    data = list(map(int, input().split()))

    # queue에서 가장 앞 요소를 가져와서 1, 2, 3, 4, 5 중 하나를 빼고 다시 큐에 넣기
    # 계속 반복하닥 한 수가 0보다 작아지면 반복을 멈추고 추력
    num = 1
    while True:
        tmp = data.pop(0) - num
        if tmp > 0:
            data.append(tmp)
        else:
            data.append(0)
            break

        num += 1
        if num == 6:
            num = 1

    print(f"#{tc}", *data)
    # print(f"#{tc}", end=' ')

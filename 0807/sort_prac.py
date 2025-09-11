T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):  # 0번부터 끝까지
        min_num, min_idx = arr[i], i  # 최소값을 현재 인덱스 값으로 업데이트
        # 남은 리스트 중 최솟값 찾기
        for j in range(i, N):  # 현재 인덱스부터
            if arr[j] < min_num:  # 만약 최소값보다 작은 값이 있다면
                min_num, min_idx = arr[j], j  # 최소값과 최소값 인덱스 업데이트

        arr[min_idx], arr[i] = arr[i], str(min_num)  # 찾은 최소값과 현재 인덱스값 교환

    print(f"#{tc} {' '.join(arr)}")
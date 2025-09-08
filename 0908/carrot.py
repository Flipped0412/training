T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot_list = list(map(int, input().split()))
    current = 0
    max_carrot = 0
    temp_max = 0

    for carrot in carrot_list:
        if carrot > current:
            current = carrot
            temp_max += 1
            if temp_max > max_carrot:
                max_carrot = temp_max
        else:
            current = carrot
            temp_max = 1

    print(f"#{tc} {max_carrot}")

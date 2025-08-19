T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_height = max(trees)
    day = 0

    for i in range(N):
        if day % 2 == 0:
            plus = 2
        else:
            plus = 1

        for j in range(N):
            if (trees[j] + plus) == max_height:
                trees[j] += plus
                day += 1
                break
        else:
            while True:
                if day % 2 == 0:
                    plus = 2
                else:
                    plus = 1

                if (trees[i] + plus) <= max_height:
                    trees[i] += plus
                    day += 1
                else:
                    break

        for k in range(N):
            if min(trees) != max_height:
                break
        else:
            break

    for i in range(N):
        if day % 2 == 0:
            plus = 2
        else:
            plus = 1

        if trees[i] < max_height:
            trees[i] += plus

        if min(trees) == max_height:
            break

        day += 1

    print(f"#{test_case} {day - 1}")

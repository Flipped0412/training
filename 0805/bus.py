# T = int(input())

# for test_case in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     bus_stop = list(map(int, input().split()))
#     charge = K
#     check = 0

#     print(charge, K, N, M, bus_stop)

#     for stop in range(N+1):
#         print('check1=========\n', stop, charge, check)
#         if charge < 0:
#             print('check2=====================')
#             check = 0
#             break

#         if (stop in bus_stop) and (bus_stop[stop + 1] - bus_stop[stop] < K):
#             charge = 3
#             check += 1
#             print('check3============\n', charge, check)

#         charge -= 1

#     print(f"#{test_case} {check}")


T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))
    charge = K
    check = 0
    tf = True
    index_num = 0

    while tf:
        if charge < 0:
            check = 0
            tf = False

        for stop_check in range(index_num+K, index_num, -1):
            if stop_check == N:
                tf = False
                break

            if stop_check in bus_stop:
                charge = K
                index_num = stop_check
                check += 1
                break

            else:
                charge -= K

    print(f"#{test_case} {check}")
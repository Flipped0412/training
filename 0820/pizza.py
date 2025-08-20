# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     pizza_lst = list(map(int, input().split()))
#     # 피자 번호와 치즈 양 매칭
#     pizza_lst = [pizza for pizza in enumerate(pizza_lst, start=1)]
#     # 오븐에 피자 넣기
#     oven = []
#
#     for i in range(N):
#         oven.append(pizza_lst.pop(0))
#
#     while len(oven) > 1:
#         # 화덕이 한 바퀴 돌면 치즈가 절반으로 녹음
#         num, cheese = oven.pop(0)
#         cheese = cheese // 2
#         # 치즈가 다 녹았으면 꺼내기
#         # 안 녹았다면 다시 화덕에 넣기
#         if cheese == 0:
#             # 꺼내고 다른 피자 넣기
#             if pizza_lst:  # 구울 피자가 남았다면
#                 pizza = pizza_lst.pop(0)
#                 oven.append(pizza)
#         else:
#             # 다시 화덕에 넣기
#             oven.append((num, cheese))
#
#     last_pizza = oven.pop(0)
#     print(f"#{test_case} {last_pizza[0]}")


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza_lst = list(map(int, input().split()))

    oven = [0] * N

    while True:
        empty = oven.count(0)
        for i in range(empty):
            oven.
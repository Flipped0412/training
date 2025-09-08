# 문제 : 동전의 최소 갯수 구하기
# 규칙 : 큰 동전부터 나누기

coin_list = [100, 50, 500, 10]
target = 1730
cnt = 0

# Greddy 문제의 단골 손님
# 정렬 연습 : 튜플? 인스턴스 리스트?
coin_list.sort(reverse=True)        # 큰 동전부터 정렬

for coin in coin_list:
    possible_cnt = target // coin   # 현재 동전으로 가능한 최대 수
    cnt += possible_cnt             # 정답에 더해주기
    target -= coin * possible_cnt   # 금액을 빼주기

print(cnt)

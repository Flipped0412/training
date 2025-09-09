# T= int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     num_li = list(map(str, input().split()))
#     num_join = ''.join(num_li)
#     current = 0
#     max_num = 1
#     check = 0

#     for index in range(1, len(num_join)):  # 인덱스 쓰려고 len 쓰기
#         intNum = int(num_join[index])  # 다음 인덱스
#         curNum = int(num_join[current])  # 현재 인덱스
#         if intNum >= curNum:  # 다음 인덱스 >= 현재인덱스 이면 단조증가
#             check = 1  # 단조 증가가 하나라도 있었다
#             current = index  # 현재 인덱스를 다음 인덱스로 변경
#         else:  # 단조 증가 규칙이 안 맞다면
#             if current == 0:  # 현재 첫번째 인덱스이면 뒤가 없엉
#                 current = index  # 인덱스 업뎃만 하고 넘기기
#                 pass
#             # 단조 증가 규칙이 안 맞는데 첫번째 인덱스도 아니면 현재 인덱스값 * 이전인덱스값 해서 최대값 비교
#             max_num = max(max_num, curNum * int(num_join[current - 1]))
#             current = index  # 인덱스 업뎃

#         if max_num == 81:  # 근데 맥스가 81이면 최대라서 더 안 해도 됨
#             break

#     if check == 0:  # 다 돌았는데 맥스넘이고 자시고 체크가 0이면 단조증가 한적 없는거라 -1 출력
#         max_num = -1

#     print(f"#{tc} {max_num}")

################################### 하.. 혜야~ 어찌 떠나려는거야 안 녕이란 그런 잔인한 말로 ########################

####### 다시 풀거야. 이해를 애초에 잘못해와부려쓰 . .  ###########
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_li = list(map(int, input().split()))
    max_multi = -1

    for index in range(1, len(num_li) - 2):
        for next_index in range(index + 1, len(num_li) - 1):
            num_multi = num_li[index] * num_li[next_index]
            if len(str(num_multi)) == 1 or str(num_multi)[0] <= str(num_multi)[1]:
                if max_multi < num_multi:
                    max_multi = num_multi

    
    print(f"#{tc} {max_multi}")
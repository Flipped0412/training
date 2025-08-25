# import math
 
# T = int(input())
 
# for test_case in range(1, T + 1):
#     N = int(input())
#     num = N // 10
#     result = 0
 
#     for i in range(1, num // 2 + 1):
#         result += int(((math.factorial(num - i) // (math.factorial(num - i - i) * math.factorial(i)))) * (2**i))
 
#     print(f"#{test_case} {result + 1}")

# def dp(n):
#     if n == 10:
#         return 1
#     elif n == 20:
#         return 3
#     return dp(n - 10) + dp(n - 20) * 2


# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     answer = dp(N)
#     print(f'#{tc} {answer}')

# T = int(input())
 
# def dfs(length):
#     global answer
#     if length == 0:
#         answer += 1
#         return
#     elif length < 0: return
 
#     # 10*20 한개 배치
#     dfs(length-10)
#     # 10*20 두개 배치
#     dfs(length-20)
#     # 20*20 한개 배치
#     dfs(length-20)
 
# for tc in range(1, T+1):
#     N = int(input())
#     answer = 0
#     dfs(N)
#     print(f'#{tc} {answer}')

V = 6
node_list = list(range(V))
print(node_list)
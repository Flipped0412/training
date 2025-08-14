# T = int(input())
#
# for test_case in range(1, T + 1):
#     words = input()
#     check_1 = 0
#     check_2 = 0
#     check_3 = 0
#     check_4 = 0
#     result = 1
#
#     for word in words:
#         if word == '{':
#             check_1 += 1
#         elif word == '}':
#             check_2 += 1
#         elif word == '(' :
#             check_3 += 1
#         elif word == ')':
#             check_4 += 1
#
#     if check_1 != check_2 or check_3 != check_4:
#         result = 0
#
#     print(f"#{test_case} {result}")

# 개웃기다. 안되는 코드만 두 개 만들었다.

T = int(input())

for test_case in range(1, T + 1):
    words = input()
    stack = []
    result = 1

    for word in words:
        if word == '{':
            stack.append(word)
        elif word == '(':
            stack.append(word)
        elif word == '}':
            if len(stack) == 0:
                result = 0
            elif stack.pop() != '{':
                result = 0
        elif word == ')':
            if len(stack) == 0:
                result = 0
            elif stack.pop() != '(':
                result = 0

    if len(stack) > 0:
        result = 0

    print(f"#{test_case} {result}")
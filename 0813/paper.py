import math

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = N // 10
    result = 0

    for i in range(1, num // 2 + 1):
        result += int(((math.factorial(num - i) // (math.factorial(num - i - i) * math.factorial(i)))) * (2**i))

    print(f"#{test_case} {result + 1}")

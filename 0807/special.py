# def select(arr, k):
#     for i in range(0, k):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[min_index] > arr[j]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr[k-1]

def select(arr, k):
    for i in range(0, k - 1):
        min_index = i
        for j in range(i + 1, k):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    sort_list = select(num_list, N)
    result = []

    for i in range(5):
        result.append(sort_list[N - i - 1])
        result.append(sort_list[i])

    print(f"#{test_case}", *result)

# 아래 함수를 수정하시오.
# def remove_duplicates_to_set(nums):
#     result = []
#     for num in nums:
#         if num not in result:
#             result.append(num)
#     return set(result)

def remove_duplicates_to_set(nums):
    return set(nums)

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

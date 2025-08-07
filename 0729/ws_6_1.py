# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    set1.update(set2)
    return set1

def union_multiple_sets(*sets):
    temp_set = sets[0]
    if len(sets) < 2:
        return '최소 두 개의 셋이 필요합니다.'

    for set in sets:
        # print(set)
        temp_set.update(set)
    
    return temp_set

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
print(result)
# 출력 : 최소 두 개의 셋이 필요합니다

for test_case in range(1, 11):
    dump_count = int(input())
    boxes = list(map(int, input().split()))

    while dump_count > 0:
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
        dump_count -= 1
    
    print(f"#{test_case} {max(boxes) - min(boxes)}")

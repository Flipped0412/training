def enqueue(item):
    global rear
    if is_full():
        print('full')
    else:
        rear = (rear + 1) % 8
        pw_q[rear] = item

def dequeue():
    global front
    if is_empty():
        print('empty')
    else:
        front = (front + 1) % 8
        return pw_q[front]
    
def is_empty():
    return front == rear

def is_full():
    return (rear + 1) % 8 == front


for test_case in range(1, 11):
    t = int(input())
    numbers = list(map(int, input().split()))
    pw_q = [0] * 8
    front = rear = 0

    
    while numbers[-1] > 0:
        for minus in range(1, 6):
            numbers[0] -= i

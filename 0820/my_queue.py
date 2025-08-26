# front = rear = 1
# q = [0]*10
#
# rear += 1
# q[rear] = 1
# rear += 1
# q[rear] = 2
# rear += 1
# q[rear] = 3
# rear += 1
# q[rear] = 4
#
# front += 1
# print(q[front])
# front += 1
# print(q[front])
# front += 1
# print(q[front])
# front += 1
# print(q[front])
#

# 큐큐큐
# 선형자료 구조
# 큐에서 사용가능한 연산 : 상ㅂ입(enqueue), 삭제(dequeue)
# 큐 구현하기 1 : 배열을 활용한 큐 구현
# 변수 2개 필요 : rear : 자료를 삽입할 위치, front : 자룔르 삭제할 위치
#   만약 rear == front 라면, queue가 비었다라고 판단
#   큐가 가득차서 더 이상 삽입이 불가한 상태 : rear가 마지막 인덱스일 때


class LinearQueue:
    def __init__(self, N):
        self.q = [None] * N
        # 삽일할 때 +1해서 그 위치에 삽입할건데
        # 0번부터 넣어야 하니까 초기값은 -1
        self.front = -1  # 가장 먼저 들어온 요소를 가리키는 변수
        self.rear = -1  # 제일 마지막 요소를 가리키는 변수

    def enqueue(self, value):
        # 제일 마지막요소 다음 칸에 삽입
        self.rear += 1
        self.q[self.rear] = value

    def dequeue(self):  # 제일 먼저 삽입된 요소를 반환하고 (삭제)
        self.front += 1
        return self.q[self.front]


# queue = LinearQueue(10)
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
#
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())

# queue.enqueue(50)  ### 선형 큐의 단점 : 요소를 안 가지고 있는데도 못 집어 넣는 경우가 발생!!
# 선형큐 --> 원형큐 로 바꿔서 해결!!
# 원형큐에서 가득 찼다라는 판단 : rear의 다음칸이 front라면 가득찼다고 판단.
#                           (rear + 1) % N == front
# 비어있는 판단 : rear == front
# 원형 큐의 시작점 : rear = 0, front = 0


class CircularQueue:
    def __init__(self, N):
        self.size = N
        self.q = [None] * N
        self.front = 0
        self.rear = 0

    def enqueue(self, value):
        next_rear = (self.rear + 1) % self.size
        if next_rear == self.front:  # 가득찬 상태
            print('큐 가득 참')
            return
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value

    def dequeue(self):
        if self.front == self.rear:  # 같으면 비어있는 상태
            print('큐가 비었어요!')
            return None

        self.front = (self.front + 1) % self.size
        return self.q[self.front]


queue = CircularQueue(10)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
queue.enqueue(500)
queue.enqueue(600)
queue.enqueue(700)
queue.enqueue(800)
queue.enqueue(900)
queue.enqueue(1000)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    # enqueue하면 노드 생성, dequeue하면 가장 먼저 enqueue된 node 삭제
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # 마지막 노드의 next에 새로운 노드의 주소값 할당
        if self.rear is None:  # 큐가 비어있다면
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

    def dequeue(self):
        # front를 반환하고 삭제
        if self.front is None:
            return None
        else:
            return_value = self.front.value
            self.front = self.front.next
            if self.front is None:  # 비어있는지 확인
                self.rear = None  # 비어있다면 이미 반환된 노드이므로 버림
            return return_value


# queue = LinkedQueue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# queue.enqueue(8)
# queue.enqueue(9)
# queue.enqueue(10)
#
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())

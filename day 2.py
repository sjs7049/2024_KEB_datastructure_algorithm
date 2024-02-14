def is_queue_empty():
    global front, rear
    return front == rear

def en_queue(data):
    global queue, rear
    rear += 1
    queue[rear] = data

def de_queue():
    global queue, front, rear
    if is_queue_empty():
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    for i in range(front + 1, rear + 1):
        queue[i - 1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1
    return data

queue = ['정국', '뷔', '지민', '진', '슈가']
front = rear = -1

if __name__ == "__main__":
    for i in queue:
        en_queue(i)
    for _ in range(rear + 1):
        print("대기 줄 상태 :", queue)
        out_person = de_queue()
        print(f"{out_person}님 식당에 들어감")

    print("대기 줄 상태 :", queue)
    print("식당 영업 종료")
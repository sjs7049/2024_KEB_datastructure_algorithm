def is_queue_full():
    global size, front
    return (rear + 1) % size == front

def is_queue_empty():
    global front, rear
    return front == rear

def en_queue(data):
    global size, queue, front, rear
    if is_queue_full():
        return
    rear = (rear + 1) % size
    queue[rear] = data

def de_queue():
    global size, queue, front, rear
    if is_queue_empty():
        return None
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None

size = 6
queue = [None for _ in range(size)]
front = rear = 0

if __name__ == "__main__":
    call_time = [('사용',9),('고장',3),('환불',4),('환불',4),('고장',3)]
    waiting_time = 0

    print("귀하의 대기 예상시간은 0분입니다.")
    print("현재 대기 콜 --->", queue)
    print()
    for call in call_time:
        en_queue(call)
        waiting_time += call[1]
        if is_queue_full():
            print("최종 대기 콜 --->", queue)
            print("프로그램 종료!")
            break
        print(f"귀하의 대기 예상시간은 {waiting_time}분입니다.")
        print("현재 대기 콜 --->", queue)
        print()


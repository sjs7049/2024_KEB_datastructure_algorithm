def de_queue() :
	global size, queue, front, rear
	if front == rear:
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None
	return data

size = 5
queue = ["화사", None, None, None, None]
front = -1
rear = 0

print(queue)
retData = de_queue()
print("추출한 데이터 -->", retData)
print(queue)
retData = de_queue()

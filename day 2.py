def pop() :
	global size, stack, top
	if top == -1:
		print("스택이 비었습니다.")
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

size = 5
stack = ["커피", None, None, None, None]
top = 0

print(stack)
retData = pop()
print("추출한 데이터 -->", retData)
print(stack)
retData = pop()

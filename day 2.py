class Node:
	def __init__ (self):
		self.data = None
		self.link = None

def print_nodes(start):
	current = start
	if current is None:
		return
	print(current.data, end=' ')
	while current.link is not None:
		current = current.link
		print(current.data, end=' ')
	print()

def delete_node(delete_data):
	global head, current, pre

	if head.data == delete_data:
		current = head
		head = head.link
		print("# 첫 노드가 삭제됨 #")
		del current
		return

	current = head
	while current.link is not None:
		pre = current
		current = current.link
		if current.data == delete_data:
			pre.link = current.link
			print("# 중간 노드가 삭제됨 #")
			del current
			return
	else:
		print("# 삭제된 노드가 없음 #")

head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
	node = Node()
	node.data = data_array[0]
	head = node

	for data in data_array[1:]:
		pre = node
		node = Node()
		node.data = data
		pre.link = node


	print_nodes(head)

	delete_node("다현")
	print_nodes(head)

	delete_node("쯔위")
	print_nodes(head)

	delete_node("사나")
	print_nodes(head)

	delete_node("재남")
	print_nodes(head)

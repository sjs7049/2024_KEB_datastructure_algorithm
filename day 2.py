class Node:
	def __init__ (self):
		self.data = None
		self.link = None

def print_nodes(start):
	current = start
	if current.link is None :
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()

def find_node(find_data):
	global head, current, pre

	current = head
	if current.data == find_data:
		print("# 첫 노드에서 찾음 #")
		return current
	while current.link != head:
		current = current.link
		if current.data == find_data:
			print("# 중간 노드에서 찾음 #")
			return current
	else:
		print("# 찾는 노드가 없음 #")
	return Node()


head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
	node = Node()
	node.data = data_array[0]
	head = node
	node.link = head

	for data in data_array[1:]:
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head

	print_nodes(head)

	fNode = find_node("다현")
	print(fNode.data)

	fNode = find_node("쯔위")
	print(fNode.data)

	fNode = find_node("재남")
	print(fNode.data)

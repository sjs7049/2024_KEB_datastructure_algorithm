class Node:
	def __init__ (self):
		self.data = None
		self.link = None

def print_nodes(start) :
	current = start
	if current is None:
		return
	print(current.data, end=' ')
	while current.link is not None:
		current = current.link
		print(current.data, end=' ')
	print()

def make_simple_linked_list(namePhone):
	global head, current, pre
	print_nodes(head)

	node = Node()
	node.data = namePhone
	if head is None:
		head = node
		return

	if head.data[1] > namePhone[1]:
		node.link = head
		head = node
		return

	current = head
	while current.link is not None :
		pre = current
		current = current.link
		if current.data[1] > namePhone[1]:
			pre.link = node
			node.link = current
			return

	current.link = node


head, current, pre = None, None, None
data_array = [["지민", "180"], ["정국", "177"], ["뷔", "183"], ["슈가", "175"], ["진", "179"]]

if __name__ == "__main__":

	for data in data_array:
		make_simple_linked_list(data)

	print_nodes(head)

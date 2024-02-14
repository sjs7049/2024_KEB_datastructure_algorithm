class Tree_node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

goods_sold = ['레쓰비캔커피','레쓰비캔커피','레쓰비캔커피', '도시락','도시락','삼각김밥',
              '레쓰비캔커피','도시락','코카콜라','삼다수','레쓰비캔커피','레쓰비캔커피',
              '레쓰비캔커피','츄팝춥스','츄팝춥스','레쓰비캔커피','코카콜라','츄팝춥스',
              '삼각김밥','코카콜라']

if __name__ == "__main__":
    print(f"오늘 판매됨 물건(중복O) --->", goods_sold)
    print('\n이진 탐색 트리 구성 완료!')

    node = Tree_node()
    node.data = goods_sold[0]
    root = node

    print("\n오늘 판매된 종류(중복X) --->", node.data, end=' ')
    for goods in goods_sold[1:]:
        node = Tree_node()
        node.data = goods
        current = root

        while True:
            if goods < current.data:
                if current.left is None:
                    current.left = node
                    print(node.data, end=' ')
                    break
                current = current.left
            elif goods > current.data:
                if current.right is None:
                    current.right = node
                    print(node.data, end=' ')
                    break
                current = current.right
            else:
                break


class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g):
    print("          ", end=' ')
    for i in range(gSize):
        print(convenience_store[i][0].rjust(5), end='     ')
    print()

    for i in range(gSize):
        print(convenience_store[i][0].rjust(10), end='   ')
        for j in range(gSize):
            print(f"{g.graph[i][j]:^2}", end='         ')
        print()
    print()

G1 = None
convenience_store = [["GS25",30], ["CU",60] , ["SEVEN11",10], ["MINISTOP",90], ["Emart24",40]]
GS25, CU, SEVEN11, MINISTOP, Emart24 = 0,1,2,3,4

gSize = 5
G1 = Graph(gSize)
G1.graph[GS25][CU] = 1; G1.graph[GS25][SEVEN11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][SEVEN11] = 1; G1.graph[CU][MINISTOP] = 1
G1.graph[SEVEN11][GS25] = 1; G1.graph[SEVEN11][CU] = 1; G1.graph[SEVEN11][MINISTOP] = 1
G1.graph[MINISTOP][CU] = 1; G1.graph[MINISTOP][SEVEN11] = 1; G1.graph[MINISTOP][Emart24] = 1
G1.graph[Emart24][MINISTOP] = 1

if __name__ == "__main__":
    print("## 편의점 그래프 ##")
    print_graph(G1)

    print("허니버터칩 최대 보유 편의점(개수) --->", end=' ')
    max_honeybutter = convenience_store[0][1]
    max_store = ''
    for i in range(1, G1.SIZE):
        if convenience_store[i][1] > max_honeybutter:
            max_honeybutter = convenience_store[i][1]
            max_store = convenience_store[i][0]

    print(f"{max_store} ({max_honeybutter})")
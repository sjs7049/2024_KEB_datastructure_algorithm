katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

def add_data(k_friend, k_cnt):
    find = -1
    for i in range(len(katok)):
        if k_cnt >= katok[i][1]:
            find = i
            break
    if find == -1:
        find = len(katok)

    insert_data(find, (k_friend, k_cnt))

def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    kLen = len(katok)

    for i in range(kLen - 1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

if __name__ == "__main__":
    name = input("추가할 친구 ---> ")
    cnt = int(input("카톡 횟수 ---> "))
    add_data(name, cnt)
    print(katok)

    name = input("추가할 친구 ---> ")
    cnt = int(input("카톡 횟수 ---> "))
    add_data(name, cnt)
    print(katok)
katok = ['다현', '정연', '쯔위', '사나', '지효']

def delete_data(position):
    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    katok_Len = len(katok)

    del katok[position: katok_Len]


delete_data(1)
print(katok)
delete_data(3)
print(katok)

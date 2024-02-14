sentences = []

def str_reverse(sen):
    return sen[::-1]

for _ in range(4):
    string = input()
    sentences.append(string)

for i in range(3,-1,-1):
    rev = str_reverse(sentences[i])
    print(rev, end='')
    print()





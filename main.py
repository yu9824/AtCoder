def LI(): return list(map(int, input().split()))
def I(): return int(input())

import sys
sys.setrecursionlimit(10 ** 9)

'''
青木派でsortして上から順番に寝返り？
得失点差でsortして上から順番に寝返り？
'''
def main(*args):
    N, AB = args

    # aoki = []
    # takahashi = []
    
    # for a, b in AB:
    #     takahashi.append(a+b)
    #     aoki.append(a)

    # 得失点差を求める
    # tokushittenn = [t + a for t, a in zip(takahashi, aoki)]


    # 得失点差を求める
    tokushittenn = []
    aoki = 0
    for a, b in AB:
        tokushittenn.append(a + b + a)
        aoki += a
    # print(aoki, tokushittenn)

    # 得失点順を降順に並べ替えて，その順番に演説していく（効果的な街の順番）
    for i, city in enumerate(argsort(tokushittenn, reverse = True)):
        aoki -= tokushittenn[city]
        if aoki < 0:
            print(i+1)
            break
        

def argsort(seq, reverse = False):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    # https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python
    return sorted(range(len(seq)), key=seq.__getitem__, reverse = reverse)



if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append([LI() for n in range(N)])
    main(*args)
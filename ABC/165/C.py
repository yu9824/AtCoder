import itertools

def main(N, M, Q, input):
    '''
    配列Aを求める→得点をreturn
    A: 長さN, 最大値Mの配列
    '''

    max_score = 0
    for i in [sorted(i) for i in list(itertools.combinations_with_replacement([i + 1 for i in range(M)], N))]:
        score = 0
        for j in range(Q):
            if i[input[j][1] - 1] - i[input[j][0] - 1] == input[j][2]: #pythonでは一つindexがずれるため．
                score += input[j][3]
        max_score = max(max_score, score)
    print(max_score)



if __name__ == '__main__':
    N, M, Q = list(map(int, input().split()))
    input = [list(map(int, input().split())) for i in range(Q)]
    main(N, M, Q, input)

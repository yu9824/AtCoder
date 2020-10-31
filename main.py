# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

'''
(a + b) - (c + d)と考える．それぞれab, cd
これの取れる範囲は 2から2 * N
'''

def main(*args):
    N, K = args

    # 範囲
    l = 2
    r = 2 * N

    ans = 0

    cd = l
    ab = cd + K
    while ab <= r:
        # print(ab, cd)
        if ab - 1 > N:
            num_ab = max(N - (ab - N) + 1, 0)
        else:
            num_ab = max(ab - 1, 0)

        if cd - 1 > N:
            num_cd = max(N - (cd - N) + 1, 0)
        else:
            num_cd = max(cd - 1, 0)
            
        ans += num_ab * num_cd

        # 次の繰り返しに向けて．
        ab += 1
        cd += 1
    print(ans)
    
    

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)



    
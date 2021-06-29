def LI(): return list(map(int, input().split()))
def I(): return int(input())

import sys
sys.setrecursionlimit(10 ** 9)

def main(*args):
    N, S = args

    st = set()
    for s in S:
        if s not in st:
            if '!' in s:
                st.add(s[1:])
            else:
                st.add(s)
        else:
            if '!' in s:
                print(s[1:])
            else:
                print(s)
            break
    else:
        print('satisfiable')


if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append({input() for n in range(N)})
    main(*args)
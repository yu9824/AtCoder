def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

# def main(*args):
    # pass    


# if __name__ == '__main__':
#     main(args)

s = input()
print(s[0] + str(len(s)-2) + s[-1])
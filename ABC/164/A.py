def main(S, W):
    if S > W:
        print('safe')
    else:
        print('unsafe')



if __name__ == '__main__':
    S, W = list(map(int, input().split()))
    main(S, W)

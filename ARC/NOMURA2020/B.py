# list(map(int, input().split()))
# int(input())

def main(T):
    ans = list(T)
    for i, s in enumerate(T):
        if s == '?':
            ans[i] = 'D'
    print(''.join(ans))
    # for i, s in enumerate(T):
    #     if s == '?':
    #         if T[i+1] != 'P':
    #             ans[i] = 'P'
    #         else:
    #             ans[i] = 'D'
    # print(''.join(ans))


if __name__ == '__main__':
    T = input()
    main(T)

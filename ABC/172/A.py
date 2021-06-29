# list(map(int, input().split()))
# int(input())

def main(S, T):
    for s, t in zip(S, T):
        print(s, t)



if __name__ == '__main__':
    S = list(input())
    T = list(input())
    main(S, T)

# list(map(int, input().split()))
# int(input())

def main(K, S):
    if len(S) > K:
        answer = S[:K] + '...'
    else:
        answer = S
    print(answer)



if __name__ == '__main__':
    K = int(input())
    S = input()
    main(K, S)

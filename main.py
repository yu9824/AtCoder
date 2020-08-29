# list(map(int, input().split()))
# int(input())

def main():
    S = input()
    T = input()
    # Sのi文字目をTの先頭として，それらの文字列の一致度を見る．

    st = set()
    for i in range(len(S)-len(T)+1):
        cnt = 0
        for s, t in zip(S[i:i+len(T)], T):
            cnt += s == t
        st.add(cnt)
    print(len(T) - max(st))


if __name__ == '__main__':
    main()

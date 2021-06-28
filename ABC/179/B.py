# list(map(int, input().split()))
# int(input())

def main():
    N = int(input())
    cnt = 0 # 連続ゾロ目カウンター
    ans = 'No'

    for n in range(N):
        if len(set(map(int, input().split()))) == 1: # ゾロ目だったら
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:    # 三回連続で出たら
            ans = 'Yes'
    else:
        print(ans)

if __name__ == '__main__':
    main()

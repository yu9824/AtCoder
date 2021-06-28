# list(map(int, input().split()))
# int(input())

def main():
    pass


if __name__ == '__main__':
    H, W, K = list(map(int, input().split()))
    HW = []
    for h in range(H):
        HW.append(list(input()))
    print(HW)

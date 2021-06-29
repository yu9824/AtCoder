# list(map(int, input().split()))
# int(input())

def main(N):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= N:
        if N % i == 0:
            lower_divisors.append(i)
            if i != N // i:
                upper_divisors.append(N//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

if __name__ == '__main__':
    N = int(input())
    {print(x) for x in main(N)}
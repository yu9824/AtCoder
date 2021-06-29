# list(map(int, input().split()))
# int(input())

from pdb import set_trace

def main():
    A, B = list(map(int, input().split()))
    print((A + B) // 2, (A - B) // 2)

if __name__ == '__main__':
    main()

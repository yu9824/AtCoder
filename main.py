# list(map(int, input().split()))
# int(input())

def main(N, A):
    # mode = 'up' or 'down'
    lst = A[:2]
    if A[0] <= A[1]:
        first_mode = 'up'
    else:
        first_mode = 'down'
    mode = first_mode

    for a in A[2:]:
        if mode == 'up':
            if lst[-1] <= a:
                lst[-1] = a
            else:
                lst.append(a)
                mode = 'down'
        else:   # mode == 'down'
            if lst[-1] >= a:
                lst[-1] = a
            else:
                lst.append(a)
                mode = 'up'

    money = 1000
    if first_mode == 'down' and len(lst) == 2:
        print(money)
        exit()
    elif first_mode == 'down':
        del lst[0]
    # else:   # first_mode == 'up'

    for n in range(len(lst) // 2):
        shou = money // lst[2*n]
        amari = money % lst[2*n]
        money = shou * lst[2*n+1] + amari
        
    print(money)




if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    main(N, A)

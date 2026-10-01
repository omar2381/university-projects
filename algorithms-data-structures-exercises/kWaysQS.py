import sys

def read_input(filename):
    A = []

    try:
        myfile = open(filename, 'r')
    except OSError:
        print('cannot open', filename)
        sys.exit(0)

    for line in myfile:
        A = A + [int(line.strip())]
    myfile.close()
    return A

def insertionsort(A):
    x = 0
    while x < len(A)-1:
        y = 0
        while y < len(A)-1:
            if A[y] > A[y+1]:
                sto = A[y]
                A[y] = A[y+1]
                A[y+1] = sto
            y = y + 1
        x = x + 1
    return A

def partition(A, k):
    x = 1
    p = []
    while x <= k :
        p.append(A[len(A) - x])
        x = x + 1
    p = insertionsort(p)
    lst = [[]]

    for i in range(len(p)):
        lst.append(p[i])
        lst.append([])

    emlst = A[0:len(A)-k]

    i = 0
    while i < len(emlst):
        x = 1
        if emlst[x] not in lst:
            while x < len(A):
                if emlst[i] > lst[x]:
                    pass
                elif emlst[i] < lst[x]:
                    lst[x-1].append(emlst[i])
                    break
                if emlst[i] > lst[len(lst)-2]:
                    lst[len(lst)-1].append(emlst[i])
                    break
                x = x + 2
        i = i + 1

    x = 0
    while x < k + 1:
        lst[x] = quicksort(lst[x],k)
        x = x + 2

    lstfinal = []
    for x in lst:
        if type(x) == list:
            lstfinal.extend(x)
        elif type(x) == int:
            lstfinal.append(x)

    return lstfinal

def quicksort(A, k):
    if len(A) < 2*k:
        A = insertionsort(A)
    else:
        A = partition(A, k)
    return A

def main():
    k = int(sys.argv[1])
    filename = sys.argv[2]
    A = read_input(filename)
    print(quicksort(A, k))

if __name__ == "__main__":
    main()
import copy
import sys


def delc(matrix, i):
    for col in matrix:
        del col[i]


def delr(matrix, i):
    del matrix[i]


def insc(table, ins, loc):
    for i in range(0, len(table)):
        if ins[i] in table[i]:
            pass
        else:
            table[i].insert(loc, (ins[i]))


def insr(table, ins, loc):
    table.insert(loc, [])
    for i in range(0, len(table)):
        if ('0.0' in table[loc]):
            pass
        else:
            table[loc].append((ins[i]))


matrix = []
file1 = open(sys.argv[1], 'r')
lines = [e for e in file1.read().split('\n') if e]
for l in lines:
    matrix.append(l.split())
file1.close()
rowsum = [0]


def first():
    for k in range(1, len(matrix)):
        rows = 0
        for m in range(1, len(matrix)):
            rows = float(rows) + float(matrix[k][m])
        rowsum.append(rows)
    for i in range(0, len(matrix)):
        print(matrix[i],rowsum[i])


first()


def vales():
    qvals = copy.deepcopy(matrix)
    colnum = len(matrix) - 2
    rowsum = [0]
    for k in range(1, len(matrix)):
        rows = 0
        for m in range(1, len(matrix)):
            rows = float(rows) + float(matrix[k][m])
        rowsum.append(rows)
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[i][0] == matrix[j][0]:
                qvals[i][j] = 0
            else:
                q = (colnum * float(matrix[i][j])) - float(rowsum[i]) - float(rowsum[j])
                qvals[i][j] = q

    for i in range(0, len(qvals)):
        print(qvals[i])

    shortest = float(qvals[1][1])
    a = 0
    b = 0
    remlet = ''

    for i in range(1, len(qvals)):
        for j in range(1, len(qvals[i])):
            if float(qvals[i][j]) != 0 and float(qvals[i][j]) < shortest:
                shortest = float(qvals[i][j])
                a = i
                b = j
                remlet = matrix[j][0]

    newin = []
    strnem = str(matrix[0][a] + (matrix[0][b]))

    for j in range(1, len(matrix)):
        if matrix[a][j] != matrix[a][0]:
            newsum = float((float(matrix[a][j]) + float(matrix[b][j]) - float(matrix[a][b])) / 2)
            newin.append(newsum)

    for i in range(len(newin) - 1, 0, -1):
        if newin[i] == 0:
            del newin[i]
            break

    newin.insert(0, strnem)

    delc(matrix, a)
    delr(matrix, a)

    for i in range(0, len(matrix)):
        if matrix[i][0] == remlet:
            todelet = i
            delc(matrix, todelet)
            delr(matrix, todelet)
            break

    insr(matrix, newin, a)
    insc(matrix, newin, a)

    rowsume = [0]
    for k in range(1, len(matrix)):
        rows = 0
        for m in range(1, len(matrix)):
            rows = float(rows) + float(matrix[k][m])
        rowsume.append(rows)

    if len(matrix) >= 3:
        for i in range(0, len(matrix)):
            print(matrix[i], rowsume[i])


def sad():
    while (len(matrix) >= 3):
        vales()


sad()
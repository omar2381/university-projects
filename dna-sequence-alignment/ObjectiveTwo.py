import time
import sys


def mat(seq1, seq2):
    score = [[0 for i in range(len(seq2)+1)] for j in range(len(seq1)+1)]
    returner = [[0 for i in range(len(seq2)+1)] for j in range(len(seq1)+1)]
    best = 0
    k = 0

    for i in range(0, len(seq1)+1):
        for j in range(0, len(seq2)+1):
            c = 0

            if i == 0 or j == 0:
                score[i][j] = 0
                returner[i][j] = 'E'

            else:
                if seq1[i-1] == seq2[j-1]:
                    if seq1[i-1] == 'A':
                        c += 3
                    elif (seq1[i-1] == 'C') or (seq1[i-1] == 'T'):
                        c += 2
                    elif seq1[i-1] == 'G':
                        c += 1
                elif seq1[i-1] == '-' or seq2[j-1] == '-':
                    c -= 4
                else:
                    c -= 3

                d = max(c + score[i - 1][j - 1], score[i - 1][j] - 4, score[i][j - 1] - 4, 0)
                score[i][j] = d
                if d >= best:
                    best = d
                    newi = i
                    newj = j

                if d == 0:
                    returner[i][j] = 'E'
                elif d == c + score[i - 1][j - 1]:
                    returner[i][j] = 'D'
                elif d == score[i - 1][j] - 4:
                    returner[i][j] = 'U'
                elif d == score[i][j - 1] - 4:
                    returner[i][j] = 'L'

    i = newi
    j = newj
    x = returner[newi][newj]

    str1 = ''
    str2 = ''

    while x != 'E':

        if x == 'D':
            str1 += seq1[i - 1]
            str2 += seq2[j - 1]
            x = returner[i - 1][j - 1]
            i = i - 1
            j = j - 1

        elif x == 'L':
            str1 += seq1[i - 1]
            str2 += '-'
            x = returner[i][j - 1]
            j = j - 1

        elif x == 'U':
            str1 += '-'
            str2 += seq2[j - 1]
            x = returner[i - 1][j]
            i = i - 1

    return str1[::-1], str2[::-1], best


def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1), len(string2))):
        if string1[i] == string2[i]:
            string3 = string3 + "|"
        else:
            string3 = string3 + " "
    print('Alignment ')
    print('String1: ' + string1)
    print('         ' + string3)
    print('String2: ' + string2 + '\n\n')


file1 = open(sys.argv[1], 'r')
seq1 = file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2 = file2.read()
file2.close()
start = time.time()

seq1, seq2, best_score = mat(seq1, seq2)
best_alignment = [seq1, seq2]

stop = time.time()
time_taken = stop - start

print('Time taken: ' + str(time_taken))
print('Best (score ' + str(best_score) + '):')
displayAlignment(best_alignment)
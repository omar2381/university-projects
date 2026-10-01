import time
import sys
import operator as op
from functools import reduce

start = time.time()

lst = []
sto1 = ''
sto2 = ''


def comb (n,r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer / denom


def compare(lst):
    x = 1
    value = lst[0][2]
    index = 0
    while x < len(lst):
        if lst[x][2] >= value:
            value = lst[x][2]
            index = x
        x = x + 1
    return value, index


def scorer(str1, str2):
    val = 0
    while len(str1) > 0:
        if str1[-1] == "A" and str2[-1] == "A":
            val += 3
        elif (str1[-1] == "C" and str2[-1] == "C") or (str1[-1] == "T" and str2[-1] == "T"):
            val += 2
        elif str1[-1] == "G" and str2[-1] == "G":
            val += 1
        elif str1[-1] == "-" or str2[-1] == "-":
            val -= 4
        else:
            val -= 3
        str1 = str1[:-1]
        str2 = str2[:-1]
    return val


def alien(sto1, sto2, seq1, seq2):
    if len(seq1) == 0 or len(seq2) == 0:
        if len(seq1) == 0:
            sto1 += "-" * len(seq2)
            sto2 += seq2
        elif len(seq2) == 0:
            sto1 += seq1
            sto2 += ("-" * len(seq1))
        lst.append([sto1, sto2, scorer(sto1,sto2)])
    else:
        alien(sto1 + seq1[0], sto2 + seq2[0], seq1[1:], seq2[1:])
        alien(sto1 + seq1[0], sto2 + "-", seq1[1:], seq2)
        alien(sto1 + "-", sto2 + seq2[0], seq1, seq2[1:])


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


def possibilities(seq1,seq2):
    x = 0
    i = 0
    if len(seq1) <= len(seq2):
        cat = len(seq1)
    else:
        cat = len(seq2)
    while i <= cat:
        x += (2**i) * comb(len(seq1), i) * comb(len(seq2), i)
        i += 1
    return x


outcomes = int(possibilities(seq1,seq2))

front = []
cate = []
back = []


def cry(seq1,seq2):
    i = 0
    j = 0
    while seq1[i] == seq2[i]:
        if seq1[i] == "A":
            j += 3
        elif seq1[i] == "C" or seq1[i] == "T":
            j += 2
        elif seq1[i] == "G":
            j += 1
        front.append(seq1[i])
        seq1 = seq1[1:]
        seq2 = seq2[1:]
    if len(seq1) == len(seq2):
        i = len(seq1)-1
        while seq1[i] == seq2[i]:
            if seq1[i] == "A":
                j += 3
            elif seq1[i] == "C" or seq1[i] == "T":
                j += 2
            elif seq1[i] == "G":
                j += 1
            back.append(seq1[i])
            seq1 = seq1[:-1]
            seq2 = seq2[:-1]
            i -= 1
    alien("", "", seq1, seq2)
    return j


test = cry(seq1,seq2)
best_score = compare(lst)
stop = time.time()
time_taken = stop - start

print('Alignments generated: ' + str(outcomes))
print('Time taken: ' + str(time_taken))
print('Best (score ' + str(best_score[0] + test) + '):')


def correction():
    x = len(front)-1
    while x <= len(front)-1 and x >= 0:
        lst[best_score[1]][0] = (str(front[x] + lst[best_score[1]][0]))
        lst[best_score[1]][1] = (str(front[x] + lst[best_score[1]][1]))
        x -= 1
    x = 0
    while x <= len(back) - 1:
        lst[best_score[1]][0] = (str(lst[best_score[1]][0] + back[x]))
        lst[best_score[1]][1] = (str(lst[best_score[1]][1] + back[x]))
        x += 1
    cate.append(lst[best_score[1]][0])
    cate.append(lst[best_score[1]][1])
    displayAlignment(cate)


correction()
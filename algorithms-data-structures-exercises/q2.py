lst = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def fact(n, k):
    start = 0
    count = 0
    checker = []
    while start <= k:
        a = 0
        checker.append(n)
        sad = len(checker)
        x = 1
        j = len(str(n))
        count = count + 1
        while j > 0:
            a = a + lst[n % 10]
            n = int(n/10)
            j = j - 1
        while x < sad:
            if checker[x] == a:
                return count-1
            x = x + 1
        n = a
        start = start + 1
    return 0


def descendants(na, nb, k):
    t = 0
    while na < nb:
        m = fact(na, k)
        na = na + 1
        if m == k:
            t = t + 1
    return t


def hammingGeneratorMatrix(r):
    n = 2** r - 1

    # construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2 ** (r - i - 1))
    for j in range(1, r):
        for k in range(2 ** j + 1, 2 ** (j + 1)):
            pi.append(k)

    # construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i + 1))

    # construct H'
    H = []
    for i in range(r, n):
        H.append(decimalToVector(pi[i], r))

    # construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n - r):
        GG.append(decimalToVector(2 ** (n - r - i - 1), n - r))

    # apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    # transpose
    G = [list(i) for i in zip(*G)]

    return G

def decimalToVector(i,l):
        lst = []
        x = 0
        while x < l:
            if i % 2 == 0:
                lst.append(0)
            else:
                lst.append(1)
            x = x + 1
            i = int(i/2)
        lst.reverse()
        return lst

def repetitionEncoder(m,n):
    return m * n

def repetitionDecoder(v):
    i = 0
    count = 0
    while i < len(v):
        if v[i] == 1:
            count = count + 1
        i = i + 1
    if count > len(v)/2:
        return [1]
    elif count < len(v)/2:
        return [0]
    else:
        return []

def message(a):
    l = len(a)
    r = 2
    k = 2 ** r - r - 1
    while k - r != (2 ** r - 2 * r - 1) or k - r < l:
        r = r + 1
        k = 2 ** r - r - 1
    lst = []
    lst.extend(decimalToVector(l, r))
    lst.extend(a)
    for i in range(r + l + 1, k + 1):
        lst.append(0)
    return lst

def hammingEncoder(m):
    l = len(m)
    lst = []
    z = 0
    r = 2
    while l != (2**r - r - 1) and r <= l:
        r = r + 1
        if r > l:
            return lst

    G = hammingGeneratorMatrix(r)
    for x in range(0, len(G[0])):
        for y in range(0, l):
            z = m[y] * G[y][x] + z
        if z > 1:
            z = 0
        lst.append(z)
        z = 0
    return lst

def hammingDecoder(v):
    l = len(v)
    r = 2
    returner = []
    val = 0

    while l != (2**r - 1) and r <= l:
        r = r + 1
        if r > l:
            return returner

    H = []
    for x in range(1, 2 ** r):
        num = decimalToVector(x, r)
        H.append(num)
    Htrans = []
    for y in range(0, len(H[0])):
        ls = []
        for k in range(0, len(H)):
            ls.append(H[k][y])
        Htrans.append(ls)

    lst = []
    for i in range(0, len(Htrans)):
        for j in range(0, len(Htrans[0])):
            val = v[j] * Htrans[i][j] + val
        if val % 2 >= 1:
            val = 1
        else:
            val = 0
        lst.append(val)
        val = 0

    res = 0
    count = len(lst) - 1
    for x in range(0, len(lst)):
        if lst[x] == 1:
            res = res + (2 ** count)
        count = count - 1

    if v[res - 1] == 1:
        v[res - 1] = 0
    else:
        v[res - 1] = 1
    returner = v

    return returner

def messageFromCodeword(c):
    l = len(c)
    r = 2
    returner = []
    lst = []

    while l != (2**r - 1) and r <= l:
        r = r + 1
        if r > l:
            return returner

    for i in range(0, r):
        lst.append(2 ** i)

    for j in range(0, l):
        if j + 1 not in lst:
            returner.append(c[j])

    return returner

def dataFromMessage(m):
    l = len(m)
    r = 2
    end = 0
    returner = []
    lst = []
    fill = []

    while l != (2**r - r - 1) and r <= l:
        r = r + 1
        if r > l:
            return returner

    lst.extend(decimalToVector(l, r))
    for i in range(0, r):
        fill.append(m[i])

    count = len(fill) - 1
    for i in range(0, len(fill)):
        if fill[i] == 1:
            end = end + 2 ** count
        count = count - 1

    if end > l:
        returner = []
    else:
        for z in range(r, r + end):
            returner.append(m[z])

    return returner

print(hammingEncoder([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]))
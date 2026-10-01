def LP(str):
    longest = 1
    n = len(str)
    p = 1
    while p < n:
        l = p - 1
        r = p
        while (l >= 0 and r < n) and (str[l] == str[r]):
            if r - l > longest:
                longest = r - l + 1
            l = l - 1
            r = r + 1
        p = p + 1
    LOPs = LOP(str)
    if longest <= LOPs:
        return LOPs
    else:
        return longest


def LP2(str):
    longest = 1
    i = 0
    while i <= len(str)-1:
        a = ""
        b = ""
        count = 0
        i = i + 1
        j = i
        while j <= len(str)-1:
            a = a + str[j]
            count = count + 1
            j = j + 1
        k = len(str) - count
        p = 0
        while p <= k-1:
            b = b + str[p]
            p = p + 1
        ret = a + b
        caller = LP(ret)
        if caller >= longest:
            longest = caller
    return longest
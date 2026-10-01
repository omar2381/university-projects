def hash_quartic (lst):
    A = ["-"]*23
    for k in lst:
        i = (4*k + 7) % 23
        count = 0
        while A[i] != '-':
            i = ((4 * k + 7) + count**4) % 23
            count = count + 1
            if count == 23:
                return A
        A[i] = k
    return(A)
def hash_double (lst):
    A = ["-"]*23
    for k in lst:
        i = (4*k + 7) % 23
        count = 0
        while A[i] != '-':
            i = ((17 - (k % 17)+i)%23)
            count = count + 1
            if count == 23:
                return A
        A[i] = k
    return(A)
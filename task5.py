def levenshatin(a, b):
    a, b = a.lower(), b.lower()
    n = len(a)
    m = len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    row_now = list(range(n + 1))
    for i in range(m + 1):
        row_past, row_now = row_now, [i] + [0] * n
        for j in range(1, n+1):
            frst, scnd, thrd = row_past[j] + 1, row_now[j - 1] + 1, row_past[j - 1]
            if a[j - 1] != b[i - 1]:
                thrd += 1
            row_now[j] = min(frst, scnd, thrd)
    return row_now[n]

print(levenshatin("Привет", "Притев"))
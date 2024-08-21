h, w, n, m = map(int, input().split())

q1, r1 = divmod(h, n+1)
q2, r2 = divmod(w, m+1)

print((q1 + int(bool(r1))) * (q2 + int(bool(r2))))
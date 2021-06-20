T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a[s - 1: e])
    print(f"b: {b}")
    res = b[k - 1]
    print(f"#{a[s - 1:e].index(res)} {res}")

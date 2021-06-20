def solution(n, k):
    cnt = 0
    for i in range(1, n):
        if n % i == 0:
            cnt += 1

        if cnt == k:
            return i
    else:
        return -1


n, k = map(int, input().split())  # 6 3
print(solution(n, k))

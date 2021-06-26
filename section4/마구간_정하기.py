def solution(n: int, k: int, lines: list) -> int:
    lt, rt = 1, max(lines)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 1
        cur = lines[0]
        for line in lines[1:]:
            if (line - cur) >= mid:
                cur = line
                cnt += 1
        if cnt >= k:
            lt = mid + 1
            res = mid
        else:
            rt = mid - 1
    return res


if __name__ == "__main__":
    import sys

    sys.stdin = open("./마구간.txt")
    n, k = map(int, input().split())
    lines = []
    for _ in range(n):
        lines.append(int(input()))
    lines.sort()

    print(solution(n, k, lines))

from typing import List


def solution(n: int, largest: int, lans: List) -> int:
    def cutLansCount(mid, lans):
        cnt = 0
        for lan in lans:
            cnt += lan // mid
        return cnt

    res = 0
    lt = 1
    rt = largest
    while lt <= rt:
        mid = (lt + rt) // 2
        if cutLansCount(mid, lans) >= n:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    return res


if __name__ == "__main__":
    import sys

    sys.stdin = open("./랜선자르기.txt", "r")
    k, n = map(int, input().split())
    lans = []
    largest = 0
    for i in range(k):
        temp = int(input())
        lans.append(temp)
        largest = max(largest, temp)

    print(solution(n, largest, lans))

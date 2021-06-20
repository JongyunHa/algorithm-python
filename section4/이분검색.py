from typing import List
import sys


def solution(m: int, arr: List) -> int:
    arr.sort()
    lp, rp = 0, len(arr) - 1

    while lp <= rp:
        mid = (lp + rp) // 2
        if m > arr[mid]:
            lp = mid + 1
        else:
            rp = mid - 1

    return mid + 1


if __name__ == "__main__":
    sys.stdin = open("./이분검색.txt", "r")
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(m, arr))

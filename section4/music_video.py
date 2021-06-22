from typing import List


def solution(n: int, m: int, music: List):
    def count(capacity: int, music: List):
        cnt = 1
        sum = 0
        for m in music:
            if sum + m > capacity:
                cnt += 1
                sum = m
            else:
                sum += m
        return cnt

    lt, rt = 1, sum(music)
    maxx = max(music)
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if mid >= maxx and count(mid, music) <= m:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1
    return res


if __name__ == "__main__":
    import sys

    sys.stdin = open("./music_video.txt", "r")
    n, m = map(int, input().split())
    music = list(map(int, input().split()))
    print(solution(n, m, music))

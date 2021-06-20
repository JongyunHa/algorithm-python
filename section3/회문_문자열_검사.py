import sys


def solution(i: int, word: str) -> str:
    def is_same(front, back):
        if front == back[::-1]:
            return f"#{i} YES"
        else:
            return f"#{i} No"

    if len(word) % 2 == 0:
        front = word[: int(len(word) / 2) + 1]
        back = word[int(len(word) / 2) :]
        return is_same(front, back)
    else:
        front = word[: int(len(word) / 2)]
        back = word[int(len(word) / 2) + 1 :]
        return is_same(front, back)


if __name__ == "__main__":
    sys.stdin = open("./회문_문자열_검사.txt", "r")
    n = int(input())
    for i in range(n):
        word = input()
        word.lower()
        print(solution(i, word))

import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

whole_paper = [list(map(int, input().split())) for _ in range(n)]


# white-0 blue-1 mix-2
def cut_paper(target_paper, x, y, size):
    if size == 1:
        return [
            target_paper[x][y],
            0 if target_paper[x][y] else 1,  # white count
            1 if target_paper[x][y] else 0,  # blue count
        ]
    half_size = size // 2

    section_1 = cut_paper(target_paper, x, y, half_size)
    section_2 = cut_paper(target_paper, x + half_size, y, half_size)
    section_3 = cut_paper(target_paper, x, y + half_size, half_size)
    section_4 = cut_paper(target_paper, x + half_size, y + half_size, half_size)

    sections = [section_1, section_2, section_3, section_4]

    if (
        section_1[0] != 2
        and section_1[0] == section_2[0]
        and section_2[0] == section_3[0]
        and section_3[0] == section_4[0]
    ):
        return [
            section_1[0],
            0 if section_1[0] == 1 else 1,
            1 if section_1[0] == 1 else 0,
        ]

    return [
        2,
        sum([x[1] for x in sections]),
        sum([x[2] for x in sections]),
    ]


paper_info = cut_paper(whole_paper, 0, 0, n)

print(paper_info[1])
print(paper_info[2])

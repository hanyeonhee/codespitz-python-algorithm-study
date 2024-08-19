import sys

N, M = 0, 0
answer = 0
L = [0] * 100001
S_nbrs = [[] for _ in range(100001)]
D_nbrs = [[] for _ in range(100001)]
impossible = False


def visit(x, v):
    global impossible
    L[x] = v
    for n in S_nbrs[x]:
        if L[n] == 3 - v:
            impossible = True
        if L[n] == 0:
            visit(n, v)
    for n in D_nbrs[x]:
        if L[n] == v:
            impossible = True
        if L[n] == 0:
            visit(n, 3 - v)


def main():
    global N, M, answer, impossible

    with open('revegetate.in', 'r') as fin:
        N, M = map(int, fin.readline().split())
        for _ in range(M):
            s, a, b = fin.readline().split()
            a, b = int(a), int(b)
            if s == "S":
                S_nbrs[a].append(b)
                S_nbrs[b].append(a)
            if s == "D":
                D_nbrs[a].append(b)
                D_nbrs[b].append(a)

    for i in range(1, N + 1):
        if not L[i]:
            visit(i, 1)
            answer += 1

    with open('revegetate.out', 'w') as fout:
        if impossible:
            fout.write("0\n")
        else:
            fout.write("1" + "0" * answer + "\n")


if __name__ == "__main__":
    main()
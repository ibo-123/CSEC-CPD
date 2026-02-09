import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Node:
    __slots__ = ("xor", "win", "size", "l", "r", "p")
    def __init__(self):
        self.xor = 0
        self.win = 0
        self.size = 0
        self.l = None
        self.r = None
        self.p = None

def pull(u):
    L, R = u.l, u.r
    u.xor = L.xor ^ R.xor
    u.size = L.size + R.size
    # winner: 0 = left, 1 = right
    if L.xor >= R.xor:
        u.win = 0
    else:
        u.win = 1

def build(arr, l, r):
    u = Node()
    if l == r:
        u.xor = arr[l]
        u.size = 1
        return u
    m = (l + r) // 2
    u.l = build(arr, l, m)
    u.r = build(arr, m + 1, r)
    u.l.p = u
    u.r.p = u
    pull(u)
    return u

def update(u):
    while u:
        pull(u)
        u = u.p

def count_above(u):
    res = 0
    while u.p:
        p = u.p
        if p.l == u:
            # you're left child
            if p.win == 1:
                res += p.r.size
        else:
            # you're right child
            if p.win == 0:
                res += p.l.size
        u = p
    return res

# ---------------- MAIN ---------------- #

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    N = 1 << n
    arr = list(map(int, input().split()))

    root = build(arr, 0, N - 1)

    # collect leaves
    leaves = [None] * N
    def collect(u, l, r):
        if l == r:
            leaves[l] = u
            return
        m = (l + r) // 2
        collect(u.l, l, m)
        collect(u.r, m + 1, r)

    collect(root, 0, N - 1)

    for _ in range(q):
        b, c = map(int, input().split())
        b -= 1

        leaf = leaves[b]
        old = leaf.xor

        # apply potion
        leaf.xor = c
        update(leaf.p)

        # compute result
        print(count_above(leaf))

        # restore
        leaf.xor = old
        update(leaf.p)

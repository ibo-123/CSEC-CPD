# from collections import defaultdict 
# n , m = map(int, input().split())
# graph = defaultdict(list)
# for i in range(m):
#         u , v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
# new_set = set()
# check_bus = True
# def check_bus_func(node):
#         global check_bus
#         if node in new_set:
#                 check_bus = False
#                 return
#         new_set.add(node)
#         for i in graph[node]:
#                 check_bus_func(i)
# check_bus_func(1)
# check_ring = True
# def check_ring_func(node, parent):
#         global check_ring
#         if node in new_set:
#                 check_ring = False
#                 return
#         new_set.add(node)
#         for i in graph[node]:
#                 if i != parent:
#                         check_ring_func(i, node)
# check_ring_func(1, -1)
# check_star = True
# def check_star_func(node):
#         global check_star
#         if node in new_set:
#                 check_star = False
#                 return
#         new_set.add(node)
#         for i in graph[node]:
#                 check_star_func(i)
# check_star_func(1)
# if check_bus:
#         print("bus topology")
# elif check_ring:
#         print("ring topology")
# elif check_star:
#         print("star topology")
n, m = map(int, input().split())

deg = [0]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1

d1 = deg.count(1)
d2 = deg.count(2)
dmax = max(deg)

if m == n and d2 == n:
    print("ring topology")

elif m == n-1 and d1 == n-1 and dmax == n-1:
    print("star topology")

elif m == n-1 and d1 == 2 and d2 == n-2:
    print("bus topology")

else:
    print("unknown topology")
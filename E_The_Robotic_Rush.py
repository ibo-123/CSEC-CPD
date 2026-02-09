import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    robots=set(map(int,input().split()))
    spikes=list(map(int,input().split()))
    gdCode=input().strip()
    D=[0]*k
    cur=0
    for i,ch in enumerate(gdCode):
        if ch=="L":
            cur-=1
        else:
            cur+=1
        D[i]=cur
    alive=len(robots)
    dead_time={}
    for i in range(k):
        v=D[i]
        to_remove=[]
        for b in spikes:
            a=b-v
            if a in robots:
                to_remove.append(a)
        for a in to_remove:
            robots.remove(a)
            alive-=1
        print(alive,end=" ")
    print()

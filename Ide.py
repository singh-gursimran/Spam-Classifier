n,k=map(int,input().split())
a = list(map(int,input().split()))
f=a[0]
h=a[-1]
p=(f*h)%1000000007
a.sort()
f=a.index(f)
h=a.index(h)
i=f
if (a[h]-a[i])>=1 and (a[h]-a[i])<=k:
    pass
else:
    i=f+1
while i!=f:
    if (a[h]-a[i])>=1 and (a[h]-a[i])<=k:
        p=(p*a[i])%1000000007
        i=i-1
    else:
        i=i+1
print(p)

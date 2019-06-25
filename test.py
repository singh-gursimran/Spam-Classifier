def pali(m):
    temp=0
    t=0
    m1=int(m)
    while m1>0:
       t=int(m1%10)
       temp=int(temp*10)+int(t)
       m1=int(m1/10)

    if temp == m:
        return True
    else:
        return False
for i in range(int(input())):
    n=int(input())
    c=100
    c1=100
    if n<10:
        if n==0:
            print(n+1)
        else:
            print(n-1)
    else:
        c1 = int(n)
        c = int(n)
        while True:

            c=c-1
            if(pali(c)==True):
                print(c)
                break
            c1=c1+1
            if (pali(c1)==True):
                print(c1)
                break

N = int(input("enter the number of integers to be added"))
L = []
for i in range(N):
    b = int(input("enter no."))
    L.append(b)
print(L)
def Largestnumber():

    a = L[0]
    for i in L:
        if i>L[0]:
            a = i
    print(a)
Largestnumber()

def Smallestnumber():
    b = L[0]
    for i in L:
        if i<L[0]:
            b = i
    print(b)

Smallestnumber()

def Sumofnumbers():
    sum=0
    for i in L:
        sum+=i
    print(sum)
Sumofnumbers()

def evenorodd():
    c=0
    d=0
    for i in L:
        if i%2==0:
            c+=1
        else:
            d+=1
    print(c)
    print(d)


evenorodd()

print(L[::-1])
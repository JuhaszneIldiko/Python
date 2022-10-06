'''szo="xenor"
print(min(szo))
print(max(szo))
betu=input("melyik betű indexe kell? ")
if betu in szo:
    print(szo.index("betu"))
else:
    print("nincs benne ilyen betű")

szo=input("kérek egy szót: ")
i=0
while i < len(szo):
    if i%2==0:
        print(szo[i].upper(), end="")
    else:
        print(szo[i], end="")
    i+=1

c=input("kérek egy szót: ")
for i in c:
    print(i.upper(), end="")
clist=list(c)
print(clist)
for i in range(len(clist)):
    print(clist[i])'''

szo=input("akármit: ")
print(min(szo))
print(max(szo))
betu=input("melyik betű: ")
if betu in szo:
    print(szo.index(betu,4,len(szo)-1))
else:
    print("nincs ilyen")

szolista=list(szo)
print(szolista)
a=int(input("masukkan angka: "))
n=int(input("masukkan pangkat: "))
def pangkat(a, n):
    if n==0 :
        return 1
    else:
        return a * pangkat(a, n-1)
print ("%d dipangkatkan %d =%d" %(a,n,pangkat(a,n)))
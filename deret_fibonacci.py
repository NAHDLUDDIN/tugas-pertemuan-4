deret1=0
deret2=1
jumlah_deret =int (input("masukkan jumlah deret : "))
for i in range (jumlah_deret):
    print (deret1, end= '')
    fibo=deret1+deret2
    deret1=deret2
    deret2=fibo
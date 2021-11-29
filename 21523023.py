#Azmi Ridho Rinanta
#21523023

#Nama
A=("Azmi Ridho Rinanta")
print(A)

#NIM
B=("21523023")
print("NIM",B)

print("")

Rumus = int(input("Pilih Rumus 1.Menghitung Debit, 2. menghitung laju gelombang : "))
if (Rumus) ==1:
    a=int(input("masukkan Volume (v) : "))
    b=int(input("masukkan Waktu (t) : "))
    c=(b/a)
    print("hasil dari penghitungan debit adalah : ",c)
elif (Rumus) ==2:
    d=int(input("masukkan frekuensi (f) : "))
    e=int(input("masukkan Debit (lambda) : "))
    f=(d*e)
    print("hasil dari penghitungan laju gelombang adalah : ",f)
else:
    print("pilih diantara nomor 1 atau 2")



    
    
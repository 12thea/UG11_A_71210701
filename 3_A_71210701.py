def hitung_hapus():
    k = input("Masukan Kalimat : ")
    is1 = int(input("Index Start : "))
    is2 = int(input("Index Stop : "))

    tjd = str(len(k))
    A = k[is1-1:is2]
    hapus = str(len(A))
    hasil = (int(hapus)/int(tjd))*100
    return hasil


print(hitung_hapus())

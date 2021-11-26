def hitung_hapus():
    k = input("Masukan Kalimat: ")
    is1 = int(input("Index Start: "))
    is2 = int(input("Index Stop: "))
    h = ((is1-is2+1)/len(k))*100
    if h < 0:
        return 0.0
    else:
        return h
print(hitung_hapus())
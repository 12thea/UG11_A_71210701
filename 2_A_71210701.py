def ambil_tengah (a,b = None):
    if b == None:
        p1 = len(a)
        p2 = (round(p1/2))
        return(a[p2])
    else:
        p1 = len(a)
        p2 = (round(p1/2))
        return (a[p2+b-1])
print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))
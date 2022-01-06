print("contoh soal yamg pertama")
nilai_mtk=int(input("masukkan nilai mtk:"))
nilai_B_inggris=int(input("masukkan nilai B.inggris:"))
nilai_B_indo=int(input("masukkan nilai B.indo:"))
minatt=int(input("masukkan minatt:"))
minat_jurusan=["1.elektro","2.mesin","3.pariwisata"]
print(minat_jurusan)
rata_rata_nilai=(nilai_mtk+nilai_B_inggris+nilai_B_indo)/3
if rata_rata_nilai <70 :
    print("anda dinyatakan tidak lolos karena skor anda adalah SKOR")
elif rata_rata_nilai==70 and rata_rata_nilai <100:
    print("Skor anda adalah SKOR, anda dinyatkan lolos ke bidang berikutnya")
    if minatt == 1:
        print("elektro")
    elif minatt == 2:
        print("mesin")
    else: 
       print("bidang pariwisata")
elif rata_rata_nilai > 70 and rata_rata_nilai <100:
    print("anda bebas memilih yang anda sukai")

print("contoh soal yang ke dua")
print("menghitung penjualan warisan tanah")
harga_jual_permeter=300000
luas_tanah=int(input("masukkan luas tanah:"))
nilai=(luas_tanah*300000)
if nilai > 100000000:
    hasil=nila-(nilai*5/100)
    print(hasil)
elif nilai > 50000000:
    hasil=nilai-(nilai*3/100)
    print(hasil)
else :
    hasil=nilai-(nilai*1/100)
    print(hasil)
    

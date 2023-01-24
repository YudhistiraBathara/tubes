print("          YB GUNSHOP        ")
print("=====================================") 

nama=input(" Nama Pelanggan : ")
tanggal=input("Tanggal Pembelian : ")
print("=====================================")
print("     ======MENU======")
print("1. MG-42                   Rp.600000000000000000")
print("2. Rheinmetall MG          Rp.300000000000000000")
print("3. Uzi Submachine gun      Rp.25000000000000000")
print("4. AK-47                   Rp.15000000000000000")
print("     ======MENU======")
h=[]
a=1 
menu_pesanan = int(input("Masukan Menu Pesanan (Nomor Menu) :  "))
if menu_pesanan == 1:
    harga = 600000000000000000
elif menu_pesanan == 2:
    harga = 300000000000000000
elif menu_pesanan == 3:
    harga =  25000000000000000
elif menu_pesanan == 4:
    harga = 15000000000000000
else :
    while True :
        print("===== Menu Tidak Tersedia silahkan Pilih Menu lainya :) ====")
        menu_pesanan=int(input("Masukan Menu Pesanan (Nomor Menu): "))
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 4:
            if menu_pesanan == 1:
                harga = 6600000000000000000
            elif menu_pesanan == 2:
                harga = 300000000000000000
            elif menu_pesanan == 3:
                harga = 25000000000000000
            elif menu_pesanan == 4:
                harga =  15000000000000000
                break
jumlah_pembelian = int(input("Masukan Jumlah Pembelian : "))
for i in range(jumlah_pembelian):
    h.append(harga)

while True:
    jawab = input("Apakah ada yang ingin ditambahkan/dikurangi? tambah/kurang/tidak ")
    if jawab == 'tambah':
        tambah = int(input("Masukan Menu Pesanan (Nomor Menu): "))
        if tambah ==1:
            harga = 6600000000000000000
        elif tambah == 2:
            harga = 300000000000000000
        elif tambah == 3:
             harga = 255000000000000000
        elif tambah == 4:
             harga = 15000000000000000
        jumlah_tambahan = int(input("Masukan Jumlah Pembelian : "))
        for i in range(jumlah_tambahan):
            h.append(harga)
        c =jumlah_tambahan+jumlah_pembelian
        print("Total Pesanan :  ",c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    elif jawab == 'kurang' :
        kurang = int(input("Berapa Jumlah yang dikurangkan ? "))
        for  i in range (kurang):
            if kurang <= 1:
                a -= kurang
                del h[a]
                bayar = sum(h)
                break
            else:
                kurang -= a
                del h[kurang]
                if kurang < 0:
                    break
        c = jumlah_pembelian - kurang 
        print("Total Pemesanan ",c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    else :
        bayar = sum(h)
        c = jumlah_pembelian
        print("Total Pemesanan", c)
        print("Total Pembayaran : Rp.{} ".format(bayar))
    break

kontak ={}

def tambah_kontak(nama,nomer):
    if nama in kontak:
        print(f"kontak dengan nama {nama} sudah ada.")
    else:
            kontak [nama]=nomor
            print(f"kontak{nama} berhasil ditmbahkan.")
            
def hapus_kontak(nama):
    if nama in kontak:
        print(f"kontak {nama} berhasil di hapus.")
    else:
            print(f"kontak dengan nama{nama} tidak ditmbahkan.")

def cari_kontak(nama):
    if nama in kontak:
        print(f"nomer telpon{nama}:{kontak[nama]}") 
    else:
            print(f"kontak dengan nama {nama}tidak ditmbahkan.")
            
def tampilkan_kontak(nama):
    if kontak:
        print("daptar kontak:") 
        for nama,nomer in kontak.items():
            print(f"{nama}:{nomor}")
    else:
                print("tidak ada kontak yg tersimpan.")


while True:
    print("\nMenu:")
    print("1.tambah kontak")
    print("2.hapus kontak")
    print("3.cari kontak")
    print("4.Tampilkan semua kontak")
    print("5.keluar")

    pilihan =input("pilih menu (1-5): ")

    if pilihan =="1":
        print("1.tambah kontak")
        nomor = input("masukannomor:")
        tambah_kontak(nama,nomer)
    elif pilihan == "2":
        nama = input("masukan nama yg ingin di hapus:")
        hapus_kontak(nama)
    elif pilihan == "3":
        nama = input("masukan nama yg ingin di cari:")
        cari_kontak(nama)
    elif pilihan == "4":
        tampilkan_kontak()
    elif pilihan == "5":
        print("keluar dari program.")
    else:
            print ("pilihan tidak di temukan.silahkan coba lagi.")
        
            

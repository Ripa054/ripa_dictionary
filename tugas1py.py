kamus = {
    "apel":"bush berwarna merah",
    "anggur":"bush kecil yg tumbung berkelompok",
    "salak":"bush berwarna coklat",
    "rambutan":"bush berwarna merah",
    "melon":"bush berwarna hijaw",
    }
kata =input("masukan kata yg ingin dicari artinya:").lower()
if kata in kamus:
    print(f"arti dari{kata} adalah {kamuas[kata]}")
else:
        print(f"maaf arti dari{kata}tidak ditemukan dalam kamus.")






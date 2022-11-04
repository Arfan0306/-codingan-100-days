while True:
    import random
    angka_rahasia = random.randint(1, 10)
    jawaban = int(input("Masukkan angka mulai dari 1 sampai 10: "))

    if jawaban == angka_rahasia:
        print("Selamat, tebakanmu benar!")
        break # berhenti paksa
    else:
        print("Tebakanmu terlalu","kecil" if jawaban < angka_rahasia else "besar")

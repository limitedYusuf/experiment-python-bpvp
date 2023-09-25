import random

kata_kata = {
    "sugeng": "selamat",
    "enjing": "pagi",
    "slamet": "selamat",
    "siyang": "siang",
    "sonten": "sore",
    "enake": "enak",
    "sing": "yang",
    "aja": "saja",
    "lho": "loh",
    "opo": "apa",
    "kula": "saya",
    "sampeyan": "anda",
    "iku": "itu",
    "wong": "orang",
    "golek": "cari",
    "waktu": "waktu",
    "salametan": "ucapan selamat",
    "jeneng": "nama",
    "kabeh": "semua",
    "seneng": "senang"
}

skor = 0
putaran = 10

for _ in range(putaran):
    kata_jawa = random.choice(list(kata_kata.keys()))
    terjemahan_benar = kata_kata[kata_jawa]

    print("Tebak kata Bahasa Jawa:")
    print(f"Kata dalam Bahasa Jawa: {kata_jawa}")

    tebakan = input("Terjemahan dalam Bahasa Indonesia: ")

    if tebakan.lower() == terjemahan_benar.lower():
        print("Selamat! Jawaban Anda benar.")
        skor += 1
    else:
        print(f"Jawaban Anda salah. Jawaban yang benar adalah: {terjemahan_benar}")

print(f"Permainan selesai! Skor Anda adalah {skor}/{putaran}")

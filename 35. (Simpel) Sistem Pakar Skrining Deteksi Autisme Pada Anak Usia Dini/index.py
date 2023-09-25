fakta = {
    'kesulitan_berkomunikasi': None,
    'sulit_berinteraksi_sosial': None,
    'perilaku_berulang_ulang': None,
    'minat_obsesi_tidak_biasa': None,
    'keterbatasan_bermain_berimajinasi': None,
    'masalah_tidur': None,
    'sulit_menunjukkan_emosi': None,
    'reaksi_terhadap_sensorik': None,
    'perkembangan_bicara_terlambat': None,
}

def tanya_pertanyaan(pertanyaan):
    while True:
        jawaban = input(pertanyaan + " (ya/tidak): ").lower()
        if jawaban == 'ya':
            return True
        elif jawaban == 'tidak':
            return False
        else:
            print("Mohon jawab dengan 'ya' atau 'tidak'.")

for gejala in fakta:
    fakta[gejala] = tanya_pertanyaan(f"Apakah anak Anda memiliki {gejala.replace('_', ' ')}?")

if (fakta['kesulitan_berkomunikasi'] and fakta['sulit_berinteraksi_sosial']) or \
   (fakta['perilaku_berulang_ulang'] and fakta['minat_obsesi_tidak_biasa']) or \
   (fakta['masalah_tidur'] and fakta['sulit_menunjukkan_emosi']) or \
   (fakta['reaksi_terhadap_sensorik'] and fakta['perkembangan_bicara_terlambat']):
    hasil = "Kemungkinan anak memiliki autisme. Mohon berkonsultasi dengan seorang spesialis."
else:
    hasil = "Kemungkinan anak tidak memiliki autisme. Namun, tetap perhatikan perkembangan anak Anda."

print("\nHasil:", hasil)

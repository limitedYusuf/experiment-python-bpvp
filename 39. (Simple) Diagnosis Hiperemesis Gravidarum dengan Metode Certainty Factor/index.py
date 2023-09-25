class CertaintyFactorSystem:
    def __init__(self):
        self.gejala = {}
        self.aturan = {}

    def tambah_gejala(self, nama_gejala, nilai_CF_HG, nilai_CF_Tidak_HG):
        self.gejala[nama_gejala] = {'HG': nilai_CF_HG, 'Tidak HG': nilai_CF_Tidak_HG}

    def tambah_aturan(self, nama_aturan, gejala_aturan):
        self.aturan[nama_aturan] = gejala_aturan

    def hitung_CF(self, gejala_terpilih):
        CF_total = 1.0
        for gejala, nilai in gejala_terpilih.items():
            CF = self.gejala[gejala][nilai]
            CF_total *= CF
        return CF_total

    def diagnosis(self, gejala_terpilih):
        CF_HG = self.hitung_CF(gejala_terpilih)
        CF_Tidak_HG = 1 - CF_HG

        if CF_HG > CF_Tidak_HG:
            return "Diagnosis: Hiperemesis Gravidarum (HG)"
        else:
            return "Diagnosis: Tidak Hiperemesis Gravidarum (Tidak HG)"

    def tampilkan_gejala(self):
        print("Daftar Gejala:")
        for i, gejala in enumerate(self.gejala, start=1):
            print(f"{i}. {gejala}: HG CF = {self.gejala[gejala]['HG']}, Tidak HG CF = {self.gejala[gejala]['Tidak HG']}")

    def input_gejala(self):
        gejala_terpilih = {}
        while True:
            self.tampilkan_gejala()
            try:
                pilihan = input("Pilih gejala (masukkan angka) atau ketik 'selesai' untuk selesai: ")
                if pilihan.lower() == 'selesai':
                    break
                pilihan = int(pilihan)
                if pilihan > 0 and pilihan <= len(self.gejala):
                    gejala = list(self.gejala.keys())[pilihan - 1]
                    nilai_gejala = input(f"Apakah '{gejala}' terjadi? (1/0): ").strip()
                    if nilai_gejala in ['1', '0']:
                        gejala_terpilih[gejala] = 'HG' if nilai_gejala == '1' else 'Tidak HG'
                    else:
                        print("Masukkan nilai yang valid (1/0).")
                else:
                    print("Pilihan tidak valid. Silakan pilih angka yang sesuai.")
            except ValueError:
                print("Masukkan angka atau 'selesai' untuk selesai.")
        return gejala_terpilih

sistem_CF = CertaintyFactorSystem()

sistem_CF.tambah_gejala('mual_parah', 0.8, 0.2)
sistem_CF.tambah_gejala('muntah_berlebihan', 0.7, 0.3)
sistem_CF.tambah_gejala('dehidrasi', 0.9, 0.1)

sistem_CF.tambah_aturan('Aturan 1', {'mual_parah': 'HG', 'muntah_berlebihan': 'HG', 'dehidrasi': 'HG'})
sistem_CF.tambah_aturan('Aturan 2', {'mual_parah': 'HG', 'muntah_berlebihan': 'Tidak HG', 'dehidrasi': 'HG'})
sistem_CF.tambah_aturan('Aturan 3', {'mual_parah': 'HG', 'muntah_berlebihan': 'HG', 'dehidrasi': 'Tidak HG'})

gejala_terpilih = sistem_CF.input_gejala()

hasil_diagnosis = sistem_CF.diagnosis(gejala_terpilih)
print(hasil_diagnosis)

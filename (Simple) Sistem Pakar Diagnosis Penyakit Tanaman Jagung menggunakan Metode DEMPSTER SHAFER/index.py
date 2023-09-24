basis_pengetahuan = {
    'P01': {'Kerusakan Daun': 'Hijau', 'Gejala': 'Bercak pada daun', 'Penyebab': 'Jamur'},
    'P02': {'Kerusakan Daun': 'Coklat', 'Gejala': 'Gugur daun', 'Penyebab': 'Hama'},
    'P03': {'Kerusakan Daun': 'Kuning', 'Gejala': 'Daun keriput', 'Penyebab': 'Kekurangan nutrisi'}
}

gejala = 'Bercak pada daun'

m = {}

for rule, data_rule in basis_pengetahuan.items():
    if data_rule['Gejala'] == gejala:
        m[rule] = 0.7

total_mass = sum(m.values())
for rule in m:
    m[rule] /= total_mass

def combine_mass(m1, m2):
    result = {}
    for r1, b1 in m1.items():
        for r2, b2 in m2.items():
            if r1 != r2:
                combination = r1 + '&' + r2
                result[combination] = b1 * b2
    return result

def total_mass(m):
    total = 1
    for belief in m.values():
        total -= belief
    return total

def compare_mass(m1, m2):
    total_m1 = total_mass(m1)
    total_m2 = total_mass(m2)
    if total_m1 > total_m2:
        return "M1 lebih kuat"
    elif total_m2 > total_m1:
        return "M2 lebih kuat"
    else:
        return "Kedua MassFunction setara"

combined_mass = m.copy()
for rule, belief in m.items():
    combined_mass = combine_mass(combined_mass, m)

print("Hasil Dempster-Shafer:")
for combination, belief in combined_mass.items():
    print(f"Kombinasi: {combination}, Kepercayaan: {belief}")

comparison = compare_mass(m, combined_mass)
print("\nPerbandingan dengan MassFunction awal:", comparison)

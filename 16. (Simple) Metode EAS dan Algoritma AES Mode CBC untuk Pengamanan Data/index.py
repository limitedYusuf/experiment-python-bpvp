import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import HMAC, SHA256
from Crypto.Util.Padding import pad, unpad

def generate_key(password, salt, key_length=32):
    return PBKDF2(password, salt, key_length, 1000000, hmac_hash_module=SHA256)

def encrypt_message(message, password):
    salt = get_random_bytes(16)
    key = generate_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC)
    padded_message = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    hmac = HMAC.new(key, ciphertext, SHA256)
    return salt + cipher.iv + ciphertext + hmac.digest()

def decrypt_message(encrypted_message, password):
    salt, iv, ciphertext, hmac_received = (
        encrypted_message[:16],
        encrypted_message[16:32],
        encrypted_message[32:-32],
        encrypted_message[-32:],
    )
    key = generate_key(password, salt)
    hmac_calculated = HMAC.new(key, ciphertext, SHA256).digest()
    
    if hmac_calculated != hmac_received:
        raise ValueError("Pesan telah diubah atau rusak!")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext)
    unpadded_message = unpad(decrypted_message, AES.block_size)
    return unpadded_message

pesan_asli = b"Yusuf adalah orang tampan dan memiliki 100 pacar waifu :*"
kata_sandi = b"KunciRahasia123"

pesan_terenkripsi = encrypt_message(pesan_asli, kata_sandi)

pesan_terdekripsi = decrypt_message(pesan_terenkripsi, kata_sandi)

print("Pesan Terenkripsi:", pesan_terenkripsi)
print("Pesan Terdekripsi:", pesan_terdekripsi.decode('utf-8'))

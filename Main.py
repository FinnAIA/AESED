import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib
import os
from tkinter import ttk

#set text box background colour
Textbox_background = "#696969"

#define encrypt_Key
def encrypt_key(key):
    salt = b'SaltForAESKey'
    key_hash = hashlib.pbkdf2_hmac('sha256', key.encode('utf-8'), salt, 100000)
    return key_hash

# Function to pad the plaintext using PKCS#7
def pad_plaintext(plaintext):
    block_size = 16
    padding_length = block_size - (len(plaintext) % block_size)
    padding = bytes([padding_length]) * padding_length
    return plaintext + padding


# Function to unpad the plaintext
def unpad_plaintext(padded_plaintext):
    padding_length = padded_plaintext[-1]
    if padding_length < 1 or padding_length > 16:
        raise ValueError("Invalid padding, text might be already decrypted")
    return padded_plaintext[:-padding_length]


def encrypt_text():
    try:
        key = key_entry.get()
        plaintext = plaintext_entry.get('1.0', 'end-1c').encode('utf-8')
        iv = get_random_bytes(16)
        cipher = AES.new(encrypt_key(key), AES.MODE_CBC, iv=iv)

        plaintext = pad_plaintext(plaintext)  # Pad the plaintext

        ciphertext = cipher.encrypt(plaintext)
        ciphertext_base64 = base64.b64encode(iv + ciphertext)
        result_text.delete('1.0', 'end')
        result_text.insert('1.0', ciphertext_base64.decode('utf-8'))

    except ValueError as ve:
        messagebox.showerror("Encryption Error", str(ve))


def decrypt_text():
    try:
        key = key_entry.get()
        ciphertext_base64 = result_text.get('1.0', 'end-1c')
        ciphertext = base64.b64decode(ciphertext_base64)
        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]
        cipher = AES.new(encrypt_key(key), AES.MODE_CBC, iv=iv)

        plaintext = cipher.decrypt(ciphertext)

        plaintext = unpad_plaintext(plaintext)  # Unpad the plaintext

        result_text.delete('1.0', 'end')
        result_text.insert('1.0', plaintext.decode('utf-8'))

    except ValueError as ve:
        messagebox.showerror("Decryption Error", str(ve))


def close_app():
    window.destroy()

window = tk.Tk()
window.title("AESED")
window.iconbitmap(r'images\Main.ico')

#set window size
window.geometry("600x450")

#change background to black
window.configure(bg="black")

# Create key entry field
key_label = tk.Label(window, text="Enter Key:", bg="black", fg="white", font=("Arial", 12, "bold"))
key_label.pack()
key_entry = tk.Entry(window, show="*", bg=Textbox_background, font=("Arial", 12))
key_entry.pack()

# Create plaintext entry field
plaintext_label = tk.Label(window, text="Enter Text:", bg="black", fg="white", font=("Arial", 12, "bold"))
plaintext_label.pack()
plaintext_entry = tk.Text(window, height=5, width=40, bg=Textbox_background, fg="white", font=("Arial", 12))
plaintext_entry.pack()

# Customize button colors and fonts
encrypt_button = tk.Button(window, text="Encypt", command=encrypt_text, bg="blue", fg="white", font=("Arial", 12, "bold"))
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text, bg="green", fg="white", font=("Arial", 12, "bold"))
exit_button = tk.Button(window, text="Exit", command=close_app, bg="red", fg="white", font=("Arial", 12, "bold"))
encrypt_button.pack()
decrypt_button.pack()
exit_button.pack()



# Create result text field
result_label = tk.Label(window, text="Result:", bg="black", fg="white", font=("Arial", 12, "bold"))
result_label.pack()
result_text = tk.Text(window, height=5, width=40, bg=Textbox_background, fg="white", font=("Arial", 12))
result_text.pack()

window.mainloop()
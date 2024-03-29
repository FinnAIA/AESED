import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib
from tkinter import ttk
import os

Textbox_background = "#696969"

def encrypt_key(key):
    salt = b'9UFLSn@j,Z<S!RI4ZW:`7VQJzwN.gh4;yZX/[m|>G/+MX3/|c\U<CTrs<u!*u+g}'
    key_hash = hashlib.pbkdf2_hmac('sha256', key.encode('utf-8'), salt, 100000)
    return key_hash

def encrypt_text():
    try:
        key = key_entry.get()
        if not key:
            messagebox.showerror("Encryption Error", "Please enter a key for encryption, error code 104")
            return
        plaintext = plaintext_entry.get('1.0', 'end-1c').encode('utf-8')
        iv = get_random_bytes(16)
        cipher = AES.new(encrypt_key(key), AES.MODE_CBC, iv=iv)
        plaintext = plaintext + b"\0" * (16 - len(plaintext) % 16)
        ciphertext = cipher.encrypt(plaintext)
        ciphertext_base64 = base64.b64encode(iv + ciphertext)
        result_text.delete('1.0', 'end')
        result_text.insert('1.0', ciphertext_base64.decode('utf-8'))
    except ValueError as ve:
        messagebox.showerror("Encryption Error", str(ve) + "\nError code 102")


def decrypt_text():
    try:
        key = key_entry.get()
        ciphertext_base64 = result_text.get('1.0', 'end-1c')
        ciphertext_with_iv = base64.b64decode(ciphertext_base64)

        if not key:
            messagebox.showerror("Decryption Error", "No key provided during encryption, error code 103")
            return

        # Extract IV and ciphertext
        iv = ciphertext_with_iv[:16]
        ciphertext = ciphertext_with_iv[16:]

        try:
            cipher = AES.new(encrypt_key(key), AES.MODE_CBC, iv=iv)
            decrypted_data = cipher.decrypt(ciphertext)

            # Remove padding
            plaintext = decrypted_data.rstrip(b"\0")

            # Display decrypted data even if an incorrect key is provided
            result_text.delete('1.0', 'end')
            result_text.insert('1.0', plaintext.decode('utf-8'))

            # Display a success message
            messagebox.showinfo("Decryption Complete", "Decryption was successful!")

        except ValueError as ve:
            # Catch ValueError related to incorrect padding
            if "incorrect padding" in str(ve):
                result_text.delete('1.0', 'end')
                result_text.insert('1.0', decrypted_data.decode('utf-8'))
                messagebox.showinfo("Decryption Complete", "Decryption was successful despite incorrect key.")
            else:
                # Display other decryption errors
                messagebox.showerror("Decryption Error", f"Decryption failed.\nError: {ve}\nError code 101")

    except ValueError as ve:
        # Display an error message without exposing specific details
        messagebox.showerror("Decryption Error", f"Decryption failed with incorrect key.\nJargon: {ve}\nError code 101")

def copy_text():
    window.clipboard_clear()
    window.clipboard_append(result_text.get('1.0', 'end-1c'))  # append new value to clipbaord

def close_app():
    window.destroy()
window = tk.Tk()
window.title("AESED")
window.iconbitmap(default=r'images\Main.ico')


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

#copy button
copy_button = tk.Button(window, text="Copy", command=copy_text, bg="blue", fg="white", font=("Arial", 12, "bold"))
copy_button.pack()

window.mainloop()
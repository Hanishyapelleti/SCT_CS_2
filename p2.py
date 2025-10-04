import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os

def encrypt_image(input_path, output_path, key=50, mode="xor"):
    img = Image.open(input_path)
    arr = np.array(img)

    if mode == "xor":
        encrypted_arr = arr ^ key
    elif mode == "add":
        encrypted_arr = (arr + key) % 256
    elif mode == "swap":
        encrypted_arr = arr[::-1]
    else:
        messagebox.showerror("Error", "Invalid mode selected!")
        return

    encrypted_img = Image.fromarray(np.uint8(encrypted_arr))
    encrypted_img.save(output_path)
    return encrypted_img

def decrypt_image(input_path, output_path, key=50, mode="xor"):
    img = Image.open(input_path)
    arr = np.array(img)

    if mode == "xor":
        decrypted_arr = arr ^ key
    elif mode == "add":
        decrypted_arr = (arr - key) % 256
    elif mode == "swap":
        decrypted_arr = arr[::-1]
    else:
        messagebox.showerror("Error", "Invalid mode selected!")
        return

    decrypted_img = Image.fromarray(np.uint8(decrypted_arr))
    decrypted_img.save(output_path)
    return decrypted_img


# -------- GUI --------
def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)

    # Show original image preview
    show_preview(file_path, label_original)


def run_encrypt():
    file_path = entry_file.get()
    if not file_path:
        messagebox.showerror("Error", "Please select an image file!")
        return

    key = int(entry_key.get()) if entry_key.get() else 50
    mode = mode_var.get()

    output_path = os.path.join(os.path.dirname(file_path), "encrypted.png")
    encrypted_img = encrypt_image(file_path, output_path, key, mode)

    if encrypted_img:
        show_preview(output_path, label_result)
        messagebox.showinfo("Success", f"Image encrypted and saved as {output_path}")


def run_decrypt():
    file_path = entry_file.get()
    if not file_path:
        messagebox.showerror("Error", "Please select an image file!")
        return

    key = int(entry_key.get()) if entry_key.get() else 50
    mode = mode_var.get()

    output_path = os.path.join(os.path.dirname(file_path), "decrypted.png")
    decrypted_img = decrypt_image(file_path, output_path, key, mode)

    if decrypted_img:
        show_preview(output_path, label_result)
        messagebox.showinfo("Success", f"Image decrypted and saved as {output_path}")


def show_preview(img_path, label_widget):
    img = Image.open(img_path)
    img.thumbnail((200, 200))  # Resize for preview
    tk_img = ImageTk.PhotoImage(img)
    label_widget.config(image=tk_img)
    label_widget.image = tk_img  # Keep a reference!


# Tkinter setup
root = tk.Tk()
root.title("Simple Image Encryption Tool with Preview")

# File selection
tk.Label(root, text="Select Image:").grid(row=0, column=0, padx=5, pady=5)
entry_file = tk.Entry(root, width=40)
entry_file.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=5, pady=5)

# Key
tk.Label(root, text="Key (default=50):").grid(row=1, column=0, padx=5, pady=5)
entry_key = tk.Entry(root, width=10)
entry_key.grid(row=1, column=1, padx=5, pady=5)

# Mode selection
tk.Label(root, text="Operation Mode:").grid(row=2, column=0, padx=5, pady=5)
mode_var = tk.StringVar(value="xor")
tk.OptionMenu(root, mode_var, "xor", "add", "swap").grid(row=2, column=1, padx=5, pady=5)

# Encrypt/Decrypt buttons
tk.Button(root, text="Encrypt", command=run_encrypt, bg="lightblue").grid(row=3, column=0, padx=5, pady=10)
tk.Button(root, text="Decrypt", command=run_decrypt, bg="lightgreen").grid(row=3, column=1, padx=5, pady=10)

# Image preview area
tk.Label(root, text="Original Image").grid(row=4, column=0, padx=5, pady=5)
tk.Label(root, text="Encrypted/Decrypted Image").grid(row=4, column=1, padx=5, pady=5)

label_original = tk.Label(root)
label_original.grid(row=5, column=0, padx=5, pady=5)

label_result = tk.Label(root)
label_result.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()

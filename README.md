# 🖼️ Simple Image Encryption Tool

This is a Python desktop application for basic image encryption and decryption, built using **Tkinter** for the GUI and **PIL (Pillow)** and **NumPy** for image processing.

It offers three simple, reversible encryption modes: XOR, simple addition, and a pixel row swap.

## ✨ Features

* **GUI Interface:** Easy-to-use graphical interface with Tkinter.
* **Multiple Modes:** Supports three basic encryption/decryption modes:
    * **XOR:** Encrypts pixels using a bitwise XOR operation with a key.
    * **Add:** Encrypts pixels by adding the key (modulo 256).
    * **Swap:** Encrypts by reversing the order of the image's pixel rows.
* **Custom Key:** Allows the user to specify a numerical key (default is 50).
* **Image Preview:** Displays the original and the processed (encrypted/decrypted) image side-by-side.
* **Supported Formats:** Works with common image file types (`.png`, `.jpg`, `.jpeg`, `.bmp`).
* **Automatic Saving:** Saves the output as `encrypted.png` or `decrypted.png` in the source image's directory.

---

## 💻 Installation and Setup

### Prerequisites

You need **Python 3.x** installed on your system. You will also need the following libraries:

1.  **Pillow (PIL):** For image manipulation.
2.  **NumPy:** For efficient array-based pixel manipulation.
3.  **Tkinter:** Usually included with standard Python installations.

### Setup Instructions

1.  **Install Dependencies:** Open your terminal or command prompt and run the following command to install Pillow and NumPy:

    ```bash
    pip install Pillow numpy
    ```

2.  **Save the Code:** Save the provided Python code as a file named `p2.py` (or `image_cipher.py`).

3.  **Run the Application:** Execute the file from your terminal:

    ```bash
    python p2.py
    ```

---

## 💡 How to Use

1.  **Select Image:** Click the **"Browse"** button to choose an image file from your computer. The file path will appear, and the original image will be displayed on the left.
2.  **Enter Key (Optional):** Enter a numerical value in the **"Key"** field. The default is `50`. (Note: The **Swap** mode does not use the key.)
3.  **Select Mode:** Choose your desired operation mode from the dropdown menu: **`xor`**, **`add`**, or **`swap`**.
4.  **Process:**
    * Click **"Encrypt"** to scramble the image pixels.
    * Click **"Decrypt"** to restore a previously encrypted image.
5.  **View and Locate Output:**
    * The processed image will appear in the **"Encrypted/Decrypted Image"** panel.
    * A success message will confirm the file has been saved as either `encrypted.png` or `decrypted.png` in the same directory as the input image.

### Important Note on Decryption

* To **decrypt** an image, you must use the **same mode** and the **same key** that were used during the encryption process.
    * *XOR:* Encrypt with key `K`, Decrypt with key `K`.
    * *Add:* Encrypt with key `K`, Decrypt with key `K`.
    * *Swap:* Encrypt using `swap` mode, Decrypt using `swap` mode.

---

## ⚙️ Core Encryption Logic

The image is first converted into a NumPy array, where each element represents a pixel's color channel value (0-255).

| Mode | Encryption Operation | Decryption Operation |
| :--- | :--- | :--- |
| **XOR** | `arr ^ key` | `arr ^ key` |
| **Add** | `(arr + key) % 256` | `(arr - key) % 256` |
| **Swap** | `arr[::-1]` (Reverse rows) | `arr[::-1]` (Reverse rows again) |

---

## 🤝 Dependencies

* [`tkinter`](https://docs.python.org/3/library/tkinter.html)
* [`Pillow`](https://pypi.org/project/Pillow/)
* [`numpy`](https://numpy.org/)

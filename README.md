# 🔐 Caesar Cipher Encryption Tool

## ✅ Project Description

This project implements a simple **Caesar Cipher algorithm** in Python
to encrypt and decrypt text messages.\
It allows the user to shift letters in the message by a fixed number of
positions in the alphabet for basic text encryption and decryption
purposes.

------------------------------------------------------------------------

## ⚡ Features

-   Encrypt plaintext using a shift value.
-   Decrypt ciphertext by reversing the shift.
-   Handles both uppercase and lowercase letters.
-   Preserves non-alphabetic characters (numbers, punctuation, spaces).
-   Interactive command-line interface (CLI).

------------------------------------------------------------------------

## ✅ How It Works

1.  **Encryption**: Each letter is shifted by a fixed number of
    positions in the alphabet (based on the user-provided shift key).
2.  **Decryption**: Reverses the encryption by shifting letters in the
    opposite direction.

Example: - Shift = 3 - Plaintext: `Hello World!` - Encrypted:
`Khoor Zruog!` - Decrypted: `Hello World!`

------------------------------------------------------------------------

## ✅ Prerequisites

-   Python 3.x

------------------------------------------------------------------------

## 🚀 Usage

1.  Run the program: `bash     python caesar_cipher.py`

2.  Follow the prompts:

    -   Choose `(e)ncrypt` or `(d)ecrypt`.
    -   Enter the message.
    -   Enter the shift value (integer).

3.  Example run:
    `Do you want to (e)ncrypt or (d)ecrypt? e     Enter the message: Hello World     Enter the shift value (an integer): 3     Encrypted message: Khoor Zruog`

------------------------------------------------------------------------

## 🎯 Purpose

This tool is designed for learning purposes to understand how simple
substitution ciphers work in cryptography.

------------------------------------------------------------------------

## 📄 License

MIT License

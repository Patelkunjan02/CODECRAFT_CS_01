def caesar_cipher_encrypt(text, shift):
    result = ""
    # Iterate through each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            # Apply the shift and handle wraparound from 'Z' to 'A'
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            # Apply the shift and handle wraparound from 'z' to 'a'
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabetic characters as they are
        else:
            result += char
    return result
def caesar_cipher_decrypt(text, shift):
      # Decryption is simply encryption with a negative shift
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    print("---------------------")

    # Get user choice for encryption or decryption
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' or 'd'.")
        return

    message = input("Enter the message: ")
    try:
        shift_value = int(input("Enter the shift value (an integer): "))
    except ValueError:
        print("Invalid shift value. Please enter a number.")
        return

    if choice == 'e':
        encrypted_text = caesar_cipher_encrypt(message, shift_value)
        print(f"Encrypted message: {encrypted_text}")
    elif choice == 'd':
        decrypted_text = caesar_cipher_decrypt(message, shift_value)
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
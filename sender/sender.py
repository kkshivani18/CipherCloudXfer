from cryptography.fernet import Fernet
import sys
import os

def generate_key():
    """Generates and saves an encryption key if not already present."""
    key_file = "encryption_key.key"
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as key_file_obj:
            key_file_obj.write(key)
        print("Encryption key saved as 'encryption_key.key'.")
    else:
        with open(key_file, "rb") as key_file_obj:
            key = key_file_obj.read()
    return key

def encrypt_file(input_file):
    """Encrypts a file using Fernet encryption."""
    key = generate_key()
    cipher = Fernet(key)

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    with open(input_file, "rb") as file:
        encrypted_data = cipher.encrypt(file.read())

    output_file = f"{input_file}.enc"
    with open(output_file, "wb") as enc_file:
        enc_file.write(encrypted_data)

    print(f"Encryption complete. Encrypted file saved as '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sender.py <file_to_encrypt>")
        sys.exit(1)

    encrypt_file(sys.argv[1])

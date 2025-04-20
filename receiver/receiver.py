from cryptography.fernet import Fernet
import sys
import os

def load_key():
    """Loads the encryption key from the file."""
    key_file = "encryption_key.key"
    if not os.path.exists(key_file):
        print("Error: Encryption key file 'encryption_key.key' not found.")
        sys.exit(1)
    with open(key_file, "rb") as key_file_obj:
        key = key_file_obj.read()
    return key

def decrypt_file(encrypted_file):
    """Decrypts an encrypted file using Fernet encryption."""
    key = load_key()
    cipher = Fernet(key)

    if not os.path.exists(encrypted_file):
        print(f"Error: File '{encrypted_file}' not found.")
        return

    with open(encrypted_file, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = cipher.decrypt(encrypted_data)
    except Exception as e:
        print("Error during decryption:", e)
        return

    # Remove .enc extension if present
    if encrypted_file.endswith(".enc"):
        output_file = encrypted_file[:-4]
    else:
        output_file = f"decrypted_{encrypted_file}"

    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted_data)

    print(f"Decryption complete. Decrypted file saved as '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python receiver.py <file_to_decrypt>")
        sys.exit(1)

    decrypt_file(sys.argv[1])

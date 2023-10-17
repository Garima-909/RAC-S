from cryptography.fernet import Fernet

class Encrypt:
    def __init__(self, data , public_key):
        self.data = data.encode()  # Convert to bytes
        # Generation of key
        self.key = public_key
        # Initialization of Fernet symmetric encryption algorithm with the key
        self.encryption_algo = Fernet(self.key)
    
    # Encrypt the data
    def encryption(self):
        encrypted_data = self.encryption_algo.encrypt(self.data)
        return encrypted_data

    # For decryption of data
    def decryption(self, encrypted_data):
        decrypted_data = self.encryption_algo.decrypt(encrypted_data)
        return decrypted_data.decode()

# Example usage
# data_to_encrypt = "Sensitive data to be encrypted"
# encryptor = Encrypt(data_to_encrypt)

# encrypted_data = encryptor.encryption()
# print("Encrypted data:", encrypted_data)

# decrypted_data = encryptor.decryption(encrypted_data)
# print("Decrypted data:", decrypted_data)

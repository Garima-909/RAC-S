import string
import random
import en


class User :
    def __init__(self) :
        pass
        
    print("User class")
    public_key = en.Fernet.generate_key()
    def UE_SEAF_en(self , SUCI) :
        user = en.Encrypt(SUCI , self.public_key)
        value = user.encryption(SUCI)
        return value
    def UE_SEAF_dc(self , SUCI) :
        user = en.Encrypt(SUCI , self.public_key)
        value = user.decryption(SUCI)
        return value

# Example
user = User()
SUCI = "Namaste India"
value = user.UE_SEAF_en(SUCI)
print(value)
value = user.UE_SEAF_dc(SUCI)
print(value)

        

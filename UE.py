import random
import hashlib
import en # self-made module


n = 45
SUCI = b"HELLO"
public_key = b"jdijfufudjf"

class UE :
    # send SUCI value to SEAF
        
    new = en.Encrypt(SUCI ,public_key)

    # This is the encrypted of SUCI
    def encryption(self) :
        encrypted_data = self.new.encryption()
        return encrypted_data

    # This is the decrypted form of SUCI
    def decryption(self) : 
        decrypted_data = self.new.decryption()  
        return decrypted_data  
    
    """
    These function will calculate the other keys
    """
    def other_keys(public_key) :
        Ke = public_key[:16] # extracing first sixteen bytes

        # Encryption of Keys starts from here , E means encrypted
        EKe = en.Encrypt(Ke , public_key)
        Kn = public_key[16:32] # extracing next sixteen bytes
        EKn = en.Encrypt(Kn , public_key)
        Ka = public_key[32:48] # extracing next sixteen bytes
        EKa = en.Encrypt(Kn , public_key)
        Ks = public_key[48:64] # extracing next sixteen bytes
        EKs = en.Encrypt(Ks , public_key)
        I = public_key[64:] # extracing remaining bytes
        EI = en.Encrypt(I , public_key)

        # Encryption of keys
        EKs.encryption()
        EKe.encryption()
        EKn.encryption()
        EKa.encryption()
        EI.encryption()

        return (EKe , EKn , EKa , EKs , EI)
    
    def authentication(self , public_key) :
        EKe , EKn , EKa , EKs , EI = self.other_keys(public_key)

        # Decryption of above keys starts from here
        ke = en.Encrypt(EKe , public_key)
        kn = en.Encrypt(EKn , public_key)
        ka = en.Encrypt(EKa , public_key)
        ks = en.Encrypt(EKs , public_key)
        i = en.Encrypt(EI , public_key)

        # Decyption starts from here
        Ke = ke.decryption()
        Kn = kn.decryption()
        Ka = ka.decryption()
        Ks = ks.decryption()
        I = i.decryption()


        # Generation AUTN and RAND values which will come from SEAF to UE.
        self.RAND = tuple((self.generate_bits(n)))
        self.AUTN = tuple((self.generate_bits(n)))
        self.XRES = tuple((self.generate_bits(n)))
        self.CK = tuple((self.generate_bits(n)))
        self.IK = tuple((self.generate_bits(n)))

        # Getting MAC address for example purpose
        self.MAC_A = self.convert_to_hash(Ke , bytes(self.RAND) + bytes(self.AUTN) + bytes(self.XRES))
        self.MAC_S = self.convert_to_hash(Ks , bytes(self.RAND) + bytes(self.AUTN) + bytes(CK) + bytes(IK))

        if (self.MAC_A == self.convert_to_hash(Ke , bytes(self.RAND) + bytes(self.AUTN) + bytes(self.XRES))) :
            RES = self.XRES
            CK = self.CK 
            IK = self.IK
        else :
            raise Exception("MAC_A verification is failed")
        

        # Generate *RES
        RES_star = self.XRES ^ self.I

        # Compute AUTN*
        AUTN_star = self.AUTN ^ self.I

        # compute MAC_S*
        MAC_S_star = self.convert_to_hash(Ks , bytes(self.RAND) + bytes(self.AUTN_star) + bytes(self.CK) + bytes(self.IK))

        if AUTN_star == self.AUTN and MAC_S_star == self.MAC_S :
            print("Authentication successfull")
        else : 
            print("Authentication failed")

    


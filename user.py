import random
import hashlib

# Taking two variables for understanding purpose
N = 97
n = 32

class User :
    '''
    It will generate random bits which will go to SEAF
    '''
    def generate_bits(bits) :
        return random.getrandbits(bits)
    

    """
    we are importing two functions in runtime , hmac module it will return a HMAC object
    hashlib = it will import all the hashing algorithms
    This below function will return a hashed_value for a given secret key and message
    for authentication use hashed_value.compare_digest() function instead of "==" to avoid hacking
    """
    def convert_to_hash(self , public_key , data) : # This function will convert data to hash form
        global key
        key = public_key
        import hmac
        import hashlib
        hashed_value = hmac.new(public_key , data , hashlib.sha128).digest() # we can use sha1 also to make it lightweight
        return hashed_value
    
    """
    These function will calculate the other keys
    """
    def other_keys(public_key) :
        Ke = public_key[:16] # extracing first sixteen bytes
        Kn = public_key[16:32] # extracing next sixteen bytes
        Ka = public_key[32:48] # extracing next sixteen bytes
        Ks = public_key[48:64] # extracing next sixteen bytes
        I = public_key[64:] # extracing remaining bytes

        return (Ke , Kn , Ka , Ks , I)
    


    
    """
    Getting authentication token from the seaf in the second run.
    This function will take care of authentication.{
        if authentication fails then UE will send the failure message to SN.
        otherwise It will calculate the res and send to SEAF.
    }
    
    This function will extract the XMAC , SQN from the autentication token and SEAF also sends RAND number.
    """

    def authentication(self , public_key) :
        Ke , Kn , Ka , Ks , I = self.other_keys(public_key)


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

    def send_MAC_A(self) :
        return self.MAC_A

    def send_MAC_S(self) :
        return self.MAC_S
            



            


    
    



        


    
    
    

        

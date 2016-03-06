import CipherInterface


class PlayFair(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""

    def __init__(self):
        print('You are using PlayFair')

    def setKey(self, key):
        self.key = key

    def encrypt(self, plaintext):
        self.plaintext = plaintext
        return self.ciphertext

    def decrypt(self, ciphertext):
        self.ciphertext = ciphertext
        return self.plaintext

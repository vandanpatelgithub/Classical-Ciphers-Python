import CipherInterface

import re

class Caesar(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""
    alpabetic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        print("You are using Caesar Cipher")

    def setKey(self, key):
        self.key = key

    def encrypt(self, plainText):

        self.plaintext = self.prepareText(plainText)

        for char in self.plaintext:
            index = self.alpabetic.index(char)
            new_index = (index + int(self.key)) % 26
            self.ciphertext += self.alpabetic[new_index]

        return self.ciphertext

    def decrypt(self, cipherText):

        self.ciphertext = self.prepareText(cipherText)

        for char in self.ciphertext:
            index = self.alpabetic.index(char)
            new_index = (index - int(self.key))

            if new_index < 0:
                new_index += 26

            self.plaintext += self.alpabetic[new_index]

        return self.plaintext

    def prepareText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        return plaintext
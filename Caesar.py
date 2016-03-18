import CipherInterface

import re

import sys

class Caesar(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""
    alpabetic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    isKey = True

    def __init__(self):
        print("You are using Caesar Cipher")

    def setKey(self, key):

        if not self.RepresentsInt(key):
            print("Key Has To Be Positive Integer")
            self.isKey = False
            sys.exit()

        elif not 0 <= int(key) <= 25:
            print("Key Has To Be In The Range of 0 to 25 [0..25]")
            self.isKey = False
            sys.exit()

        self.key = key

        return self.isKey

    def encrypt(self, plainText):

        if self.isKey:

            self.plaintext = self.prepareText(plainText)

            for char in self.plaintext:
                index = self.alpabetic.index(char)
                new_index = (index + int(self.key)) % 26
                self.ciphertext += self.alpabetic[new_index]

            return self.ciphertext

        else:

            print("Something is wrong with the key!")
            sys.exit()

    def decrypt(self, cipherText):

        if self.isKey:

            self.ciphertext = self.prepareText(cipherText)

            for char in self.ciphertext:
                index = self.alpabetic.index(char)
                new_index = (index - int(self.key))

                if new_index < 0:
                    new_index += 26

                self.plaintext += self.alpabetic[new_index]

            return self.plaintext

        else:

            print("Something is wrong with the key !")
            sys.exit()

    def prepareText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        return plaintext

    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
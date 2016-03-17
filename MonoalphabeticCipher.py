import CipherInterface

from collections import OrderedDict

import sys

import re


class MonoalphabeticCipher(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""

    def __init__(self):
        print("You are using Monoalphabetic Cipher")

    def setKey(self, key):

        newkey = "".join(OrderedDict.fromkeys(key))

        self.key = newkey

        key_length = int(len(self.key))

        if key_length is not 26:
            print("Key has to be exactly 26 unique characters")
            sys.exit()

    def encrypt(self, plainText):

        self.plaintext = self.prepareText(plainText)

        alphabetic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        print(self.key)

        print(self.plaintext)

        for letter in self.plaintext:
            index = alphabetic.index(letter)
            self.ciphertext += self.key[index]

        print(self.ciphertext)

        return self.ciphertext

    def decrypt(self, cipherText):

        self.ciphertext = self.prepareText(cipherText)

        alphabetic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for letter in self.ciphertext:
            index = self.key.index(letter)
            self.plaintext += alphabetic[index]

        print(self.plaintext)
        return self.plaintext

    def prepareText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        return plaintext
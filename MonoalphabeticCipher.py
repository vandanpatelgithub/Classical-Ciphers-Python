import CipherInterface

from collections import OrderedDict

import sys

import re


class MonoalphabeticCipher(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""
    isKey = True

    def __init__(self):
        print("You are using Monoalphabetic Cipher")

    def setKey(self, key):

        newkey = "".join(OrderedDict.fromkeys(key))

        if not newkey.isalpha():
            print("Key can only contain alphabets")
            self.isKey = False
            sys.exit()

        key_length = int(len(newkey))

        if key_length is not 26:
            print("Key length is : " + str(key_length))
            print("Key has to be exactly 26 unique characters")
            self.isKey = False
            sys.exit()

        self.key = newkey

        return self.isKey

    def encrypt(self, plainText):

        if self.isKey:

            self.plaintext = self.prepareText(plainText)

            alphabetic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            for letter in self.plaintext:
                index = alphabetic.index(letter)
                self.ciphertext += self.key[index]

            return self.ciphertext

        else:

            print("Something is wrong with Key!")
            sys.exit()

    def decrypt(self, cipherText):

        if self.isKey:

            self.ciphertext = self.prepareText(cipherText)

            alphabetic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            for letter in self.ciphertext:
                index = self.key.index(letter)
                self.plaintext += alphabetic[index]

            return self.plaintext

        else:

            print("Something is wrong with Key!")
            sys.exit()

    def prepareText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        return plaintext
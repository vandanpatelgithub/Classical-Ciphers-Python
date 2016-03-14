import CipherInterface

import re


class RowTransposition(CipherInterface.CipherInterface):
    key = ""
    plaintext = ""
    ciphertext = ""

    def __init__(self):
        print("You are using Row Transposition")

    def setKey(self, key):
        newkey = key.split(' ')
        newkey = map(int, newkey)
        self.key = newkey

    def encrypt(self, plaintext):

        self.plaintext = plaintext

        prepared_text = self.prepateText(self.plaintext)

        key_length = len(self.key)

        length_prepared_text = len(prepared_text)

        for keys in self.key:
            index = keys - 1
            while index < length_prepared_text:
                self.ciphertext += prepared_text[index]
                index += key_length

        return self.ciphertext

    def decrypt(self, ciphertext):
        return self.plaintext

    def prepateText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        maxValue = len(self.key)

        text_length = len(plaintext)

        if text_length % maxValue != 0:
            padding_length = maxValue - (text_length % maxValue)

            for e in range(padding_length):
                plaintext += 'X'

        return plaintext


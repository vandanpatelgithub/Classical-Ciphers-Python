import CipherInterface

import re


class RailFence(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""
    start, end = 0, 0

    def __init__(self):
        print("You are using RailFence")

    def setKey(self, key):
        self.key = key

    def encrypt(self, plainText):

        self.plaintext = self.prepareText(plainText)

        plaintext_length = len(self.plaintext)

        depth = int(self.key)

        depth_list = [self.plaintext[i:i+depth] for i in range(0, len(self.plaintext), depth)]

        print(depth_list)

        depth_counter = 0

        while depth_counter < depth:
            for lists in depth_list:
                    length = len(lists)
                    if depth_counter < length:
                        self.ciphertext += lists[depth_counter]
            depth_counter += 1

        return self.ciphertext

    def decrypt(self, cipherText):

        counter, length_counter = 0, 0

        ciphertext_list = []

        self.ciphertext = cipherText

        print(self.ciphertext)

        ciphertext_length = len(self.ciphertext)

        depth = int(self.key)

        rows = ciphertext_length / depth

        remaining_letters = ciphertext_length % depth

        while counter < depth:

            if remaining_letters > 0:
                self.end += rows + 1
                ciphertext_list.append(self.ciphertext[self.start:self.end])
                remaining_letters -= 1
                self.start = self.end
                counter += 1
            else:
                self.end += rows
                ciphertext_list.append(self.ciphertext[self.start:self.end])
                self.start = self.end
                counter += 1

        max_length = len(ciphertext_list[0])

        while length_counter < max_length:
            for lists in ciphertext_list:
                length = len(lists)
                if length_counter < length:
                    self.plaintext += lists[length_counter]
            length_counter += 1

        print(self.plaintext)

        return self.plaintext

    def prepareText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        return plaintext
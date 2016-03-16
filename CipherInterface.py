import abc


class CipherInterface():
    __metaclass__ = abc.ABCMeta

    className = ""

    @abc.abstractmethod
    def setKey(self, key):
        pass

    @abc.abstractmethod
    def encrypt(self, plainText):
        pass

    @abc.abstractmethod
    def decrypt(self, cipherText):
        pass

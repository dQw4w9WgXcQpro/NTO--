from sage.all import *
from string import printable
import json

class DihedralCrypto:
    def __init__(self, order: int) -> None:
        self.__G = DihedralGroup(order)
        self.__order = order
        self.__gen = self.__G.gens()[0]
        self.__list = self.__G.list()
        self.__padder = 31337

    def __pow(self, element, exponent: int):
        try:
            element = self.__G(element)
        except:
            raise Exception("Not Dihedral rotation element")
        answer = self.__G(())
        aggregator = element
        for bit in bin(int(exponent))[2:][::-1]:
            if bit == '1':
                answer *= aggregator
            aggregator *= aggregator
        return answer

    def __byte_to_dihedral(self, byte: int):
        return self.__pow(self.__gen, byte * self.__padder)

    def __map(self, element):
        return self.__list.index(element)

    def __unmap(self, index):
        return self.__list[index]

    def hash(self, msg):
        answer = []
        for byte in msg:
            answer.append(self.__map(self.__byte_to_dihedral(byte)))
        return answer


if __name__ == "__main__":
    dihedral = DihedralCrypto(1337)
    correct = [277, 92, 775, 480, 160, 92, 31, 586, 277, 801, 355, 489, 801, 31, 62, 926, 725, 489, 160, 92, 31, 586, 277, 801, 355, 489, 1281, 62, 801,
               489, 1175, 277, 453, 489, 453, 348, 725, 31, 348, 864, 864, 348, 453, 489, 737, 288, 453, 489, 889, 804, 96, 489, 801, 721, 775, 926, 1281, 631]
    chardict = {}
    for c in printable:
        answer = dihedral.hash(c.encode())
        chardict[answer[0]] = c
    for num in correct:
        print(chardict[num],end='')
    with open('hashed', 'w') as f:
        f.write(json.dumps(chardict))

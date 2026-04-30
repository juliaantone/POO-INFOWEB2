import random
class Bingo():
    def __int__(self, numBolas):
        self.numBolas = numBolas
        self.bolas = []
    def sortear(self):
        if len(self.bolas) >= self.numBolas:
            return None
        while True:
            num = random.randint(1, self.numBolas)
            if num not in self.bolas:
                self.bolas.append(num)
                return num
    def sorteados(self):
        return self.bolas
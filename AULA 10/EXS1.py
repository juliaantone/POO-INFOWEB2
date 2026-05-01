class Viagem:
    def __init__(self, des, dis, l):
        self.set_destino(des)
        self.set_distancia(dis)
        self.set_litros(l)
    def set_destino(self, destino):
        if len(destino) >= 5: 
            self.__destino = destino
        else: raise ValueError()
    def set_distancia(self,distancia):
        if distancia > 0:
             self.__distancia = distancia
        else: raise ValueError()
    def set_litros(self, litros):
        if litros > 0:
            self.__litros = litros
        else: raise ValueError()
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia / self.__litros
    def __str__(self):
        return (f"DESTINO: {self.__destino}\n"
                f"DISTÂNCIA: {self.__distancia:.2f} km\n"
                f"COMBUSTÍVEL: {self.__litros:.2f} L")
    

class ViagemUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1: 
                ViagemUI.calculo
                
    @staticmethod
    def menu():
        print("-" * 50)
        print("1. CALCULAR")
        print("2. FIM")
        return int(input("ESCOLHA UMA OPÇÃO: "))
    
    @staticmethod
    def calculo():
        des = input("QUAL FOI O SEU DESTINO NA VIAGEM? ")
        dis = float(input("QUALA DISTÂNCIA PERCORRIDA EM KM? "))
        l = float(input("QUANTOS LITROSDE COMBUTÍVEL FOROM GASTOS? "))
        v = Viagem(des, dis, l)
        print(v)

ViagemUI.main()
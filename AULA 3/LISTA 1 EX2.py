class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.horas = horas
        self.minutos = minutos
    def calcular_velocidade_media(self):
        tempo_total_horas = self.horas + (self.minutos / 60)
        if tempo_total_horas == 0:
            return 0 
        return self.distancia / tempo_total_horas

distancia = float(input("Digite a distância da viagem (km): "))
horas = int(input("Digite as horas da viagem: "))
minutos = int(input("Digite os minutos da viagem: "))
v = Viagem(distancia, horas, minutos)
velocidade = v.calcular_velocidade_media()
print(f"Velocidade média da viagem: {velocidade:.2f} km/h")
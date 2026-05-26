from datetime import datetime
s = input("Infome sua data de nascimento dd/mm/aa: ")
print(s)
data = datetime.strptime(s, "%d/%m/%Y")
print(data)
print(data.strftime("%d/%m/%Y")) 
print(data.weekday()) # 0 - Seg, 1 - Ter

# strftime - passa uma data para string
# strptime - passa uma datetime para string

x = int(input("Informe um número: "))
x = datetime.strptime(input("Informe uma data: "), "%d/%m/%Y")
print(data.weekday()) # 0 - Seg, 1 - Ter
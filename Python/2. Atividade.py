casada: str

nome = input("Digite seu nome: ")
sexo =  input("Digite seu sexo: ")
estadoCivil = input("Digite seu estado civil: ")

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "Feminino" and estadoCivil == "casada":
    tempodeCasada = input("Digite seu tempo de casada em anos: ")

print("===Exibindo dados ===")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estadoCivil}")

if sexo == "Feminino" and estadoCivil == "casada":
    tempodeCasada = int(input("Digite seu tempo de casada em anos: "))
print(f"Tempo de casada: {tempodeCasada}")
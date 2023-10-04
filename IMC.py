altura = peso = imc = None

altura = float(input("Qual a sua altura?"))
peso = float(input("Qual o seu peso?"))

imc = peso / altura**2

print(f"seu IMC é{imc}");

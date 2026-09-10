# Calculadora de IMC


def ler_dados():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    return peso, altura


def calcular_imc(peso, altura):
    return peso / (altura * altura)


def main():
    print("Calculadora de IMC")
    peso, altura = ler_dados()
    imc = calcular_imc(peso, altura)
    print("Seu IMC e: %.2f" % imc)


if __name__ == "__main__":
    main()

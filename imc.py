# Calculadora de IMC


def ler_dados():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    return peso, altura


def calcular_imc(peso, altura):
    return peso / (altura * altura)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepesso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


def main():
    print("Calculadora de IMC")
    peso, altura = ler_dados()
    imc = calcular_imc(peso, altura)
    print("Seu IMC e: %.2f" % imc)
    print("Classificacao: %s" % classificar_imc(imc))


if __name__ == "__main__":
    main()

# Calculadora de IMC


def ler_dados():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    return peso, altura


def main():
    print("Calculadora de IMC")
    peso, altura = ler_dados()
    print("Peso informado:", peso)
    print("Altura informada:", altura)


if __name__ == "__main__":
    main()

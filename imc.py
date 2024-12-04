# Função para calcular o IMC
def calcular_imc(peso, altura):
    # IMC = peso / (altura * altura)
    imc = peso / (altura ** 2)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3 (Obesidade mórbida)"

# Função principal
def main():
    print("Calculadora de IMC")
    
    # Solicita ao usuário o peso e altura
    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            return
        
        # Calcula o IMC
        imc = calcular_imc(peso, altura)
        
        # Classifica o IMC
        classificacao = classificar_imc(imc)
        
        # Exibe o resultado
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    
    except ValueError:
        print("Por favor, insira um número válido para peso e altura.")

# Chama a função principal para rodar o programa
if __name__ == "__main__":
    main()

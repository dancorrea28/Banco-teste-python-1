class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Operação inválida! Digite um valor válido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


def main():
    conta = ContaBancaria()

    while True:
        print("\n=== MENU ===")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Verificar Saldo")
        print("[4] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.verificar_saldo()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

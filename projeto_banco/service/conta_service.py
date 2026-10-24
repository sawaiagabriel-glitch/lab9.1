class ContaService:

    def depositar(self, conta, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")

        conta.depositar(valor)

    def sacar(self, conta, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")

        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente.")

        conta.sacar(valor)
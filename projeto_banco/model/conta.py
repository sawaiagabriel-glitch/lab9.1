from datetime import datetime


class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo
        self._historico = []

    def depositar(self, valor):
        self.saldo += valor

        self._historico.append({
            "tipo": "Depósito",
            "valor": valor,
            "data": datetime.now()
        })

    def sacar(self, valor):
        self.saldo -= valor

        self._historico.append({
            "tipo": "Saque",
            "valor": valor,
            "data": datetime.now()
        })

    @property
    def historico(self):
        return self._historico
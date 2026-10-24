from model.cliente import Cliente
from model.conta import Conta
from service.conta_service import ContaService


class ContaController:
    def __init__(self, view):
        self.view = view
        self.conta = None
        self.service = ContaService()

        self.view.botao_criar.config(command=self.criar_conta)
        self.view.botao_depositar.config(command=self.depositar)
        self.view.botao_sacar.config(command=self.sacar)
        self.view.botao_historico.config(command=self.mostrar_historico)

    def criar_conta(self):
        try:
            nome, cpf, saldo = self.view.obter_dados_conta()

            saldo = float(saldo)

            cliente = Cliente(nome, cpf)
            self.conta = Conta(cliente, saldo)

            self.view.exibir_conta(self.conta)

        except ValueError as erro:
            self.view.exibir_erro(str(erro))

    def depositar(self):
        try:
            if self.conta is None:
                raise ValueError("Crie uma conta primeiro.")

            valor = float(self.view.obter_valor_movimentacao())

            self.service.depositar(self.conta, valor)

            self.view.exibir_conta(self.conta)
            self.view.limpar_valor()

        except ValueError as erro:
            self.view.exibir_erro(str(erro))

    def sacar(self):
        try:
            if self.conta is None:
                raise ValueError("Crie uma conta primeiro.")

            valor = float(self.view.obter_valor_movimentacao())

            self.service.sacar(self.conta, valor)

            self.view.exibir_conta(self.conta)
            self.view.limpar_valor()

        except ValueError as erro:
            self.view.exibir_erro(str(erro))

    def mostrar_historico(self):
        try:
            if self.conta is None:
                raise ValueError("Crie uma conta primeiro.")

            self.view.exibir_historico(self.conta.historico)

        except ValueError as erro:
            self.view.exibir_erro(str(erro))
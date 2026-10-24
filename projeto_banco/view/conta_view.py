import tkinter as tk
from tkinter import messagebox


class ContaView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento Bancário")
        self.root.geometry("430x600")

        tk.Label(root, text="Nome:").pack(pady=5)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()

        tk.Label(root, text="CPF:").pack(pady=5)
        self.cpf_entry = tk.Entry(root)
        self.cpf_entry.pack()

        tk.Label(root, text="Saldo Inicial:").pack(pady=5)
        self.saldo_entry = tk.Entry(root)
        self.saldo_entry.pack()

        self.botao_criar = tk.Button(root, text="Criar Conta")
        self.botao_criar.pack(pady=10)

        self.resultado = tk.Label(root, text="", justify="left")
        self.resultado.pack(pady=10)

        tk.Label(root, text="Valor da operação:").pack(pady=5)
        self.valor_entry = tk.Entry(root)
        self.valor_entry.pack()

        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10)

        self.botao_depositar = tk.Button(frame_botoes, text="Depositar")
        self.botao_depositar.pack(side=tk.LEFT, padx=5)

        self.botao_sacar = tk.Button(frame_botoes, text="Sacar")
        self.botao_sacar.pack(side=tk.LEFT, padx=5)

        self.botao_historico = tk.Button(root, text="Ver Histórico")
        self.botao_historico.pack(pady=10)

        self.historico_text = tk.Text(root, height=10, width=48, state="disabled")
        self.historico_text.pack(pady=10)

    def obter_dados_conta(self):
        return (
            self.nome_entry.get().strip(),
            self.cpf_entry.get().strip(),
            self.saldo_entry.get().strip()
        )

    def obter_valor_movimentacao(self):
        return self.valor_entry.get().strip()

    def limpar_valor(self):
        self.valor_entry.delete(0, tk.END)

    def exibir_conta(self, conta):
        texto = (
            f"Conta ativa\n\n"
            f"Nome: {conta.cliente.nome}\n"
            f"CPF: {conta.cliente.cpf}\n"
            f"Saldo: R$ {conta.saldo:.2f}"
        )
        self.resultado.config(text=texto)

    def exibir_historico(self, historico):
        self.historico_text.config(state="normal")
        self.historico_text.delete("1.0", tk.END)

        if not historico:
            self.historico_text.insert(tk.END, "Nenhuma movimentação registrada.")
        else:
            for operacao in historico:
                data = operacao["data"].strftime("%d/%m/%Y %H:%M:%S")
                linha = (
                    f'{data} - {operacao["tipo"]}: '
                    f'R$ {operacao["valor"]:.2f}\n'
                )
                self.historico_text.insert(tk.END, linha)

        self.historico_text.config(state="disabled")

    def exibir_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)
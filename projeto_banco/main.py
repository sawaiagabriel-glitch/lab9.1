import tkinter as tk

from controller.conta_controller import ContaController
from view.conta_view import ContaView


root = tk.Tk()

view = ContaView(root)
controller = ContaController(view)

root.mainloop()
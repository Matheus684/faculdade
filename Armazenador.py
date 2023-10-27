import tkinter as tk
import subprocess
import os

c = os.path.dirname(__file__)
nomeArquivo = c + "\\Pontuacao.txt"

def gravar_dados(text):#r
    print(text)
    arquivo = open(nomeArquivo, "a")
    arquivo.write("Nome: %s" % entry_name.get().upper())
    arquivo.write("\n")
    arquivo.close()

def start_game():#r
    character_name = entry_name.get()
    subprocess.run(["python", "jogo.py", character_name])  # Passando o character_name como argumento

window = tk.Tk()
window.configure(background='DarkSeaGreen')
window.title("NOME DO JOGO")
window.resizable(False, False)

name_label = tk.Label(window, text="Username: ")
name_label.grid(column=0, row=0)
name_label.configure(background='Silver')

entry_name = tk.Entry(window)
entry_name.grid(column=1, row=0)

botao_iniciar = tk.Button(window, text="Start Game", command=start_game)
botao_iniciar.grid(column=4, row=2)
botao_iniciar.configure(border='5', background='lightblue')

botao_dois = tk.Button(window, text="Gravar", command=lambda: gravar_dados(entry_name.get()))
botao_dois.grid(column=4, row=0)
botao_dois.configure(border='5', background='lightblue')

message = tk.Label(window, text="")
message.grid(column=3, row=4)

window.mainloop()

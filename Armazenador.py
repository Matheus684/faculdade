import tkinter as tk
import subprocess
import os

# Obtém o diretório atual do script
c = os.path.dirname(__file__)
nomeArquivo = os.path.join(c, "Pontuacao.txt")

'''def calcular_media_jogadores():
    with open(nomeArquivo, "r") as arquivo:
        dados = arquivo.readlines()
        pontuacoes = [int(dado.split(": ")[1]) for dado in dados if dado.startswith("Pontos:")]
        if pontuacoes:
            media = sum(pontuacoes) / len(pontuacoes)
            with open(nomeArquivo, "a") as arquivo:
                arquivo.write(f"Media de Pontos: {media}\n")'''

def gravar_dados_e_iniciar():
    nome = entry_name.get().strip().upper()
    if nome:
        with open(nomeArquivo, "a") as arquivo:
            arquivo.write(f"Nome: {nome}\n")
        subprocess.run(["python", "jogo.py", nome])
        #calcular_media_jogadores()

# Configuração da janela principal
window = tk.Tk()
window.title("NOME DO JOGO")
window.geometry("300x150")
window.resizable(False, False)
window.configure(background='DarkSeaGreen')

# Configuração dos elementos visuais
title_label = tk.Label(window, text="Bem-vindo ao Jogo!", font=("Arial", 14, "bold"), bg='DarkSeaGreen', fg='white')
title_label.pack(pady=10)

name_label = tk.Label(window, text="Nome de Usuário:", bg='DarkSeaGreen', fg='white')
name_label.pack(pady=5)

entry_name = tk.Entry(window, width=30)
entry_name.pack(pady=5)

button_frame = tk.Frame(window, bg='DarkSeaGreen')
button_frame.pack(pady=5)

botao_iniciar_e_gravar = tk.Button(button_frame, text="Iniciar Jogo", command=gravar_dados_e_iniciar, bg='lightblue', fg='white')
botao_iniciar_e_gravar.pack(padx=5, pady=5)

message = tk.Label(window, text="", bg='DarkSeaGreen', fg='white')
message.pack(pady=5)

window.mainloop()

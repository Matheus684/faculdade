from tkinter import *
import os


c = os.path.dirname(__file__)
nomeArquivo = c + "\\Pontuacao.txt"
def gravar_dados(text):
    print(text)
    arquivo = open(nomeArquivo, "a")
    arquivo.write("Nome: %s" % unome.get())
    arquivo.write("\n")
    #arquivo.write(DinoGamer.gravar_dados('pontos: %s' % DinoGamer.pontos))
    arquivo.close()

    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()

'''e = os.path.dirname(__file__)
nomeArquivo = e + "\\Pontuacao.txt"

def gravar_pontos(number):
    print(number)
    documento = open(nomeArquivo, "a")
    documento.write("pontos: %s" % DinoGamer.texto_pontos)
    documento.write("\n")
    documento.close()'''

janela = Tk()
janela.title("Armazenador")  # titulo da janela
janela.configure(bg='Black', )

texto = Label(janela, text="insira seu nome aqui:", background='Darkgreen')  # seria uma descriçao
texto.grid(column=0, row=0)  # tamanho

unome = Entry(janela, width=50)
unome.grid(column=0, row=1)

botao = Button(janela, text="Gravar", command=lambda: gravar_dados(unome.get()))
botao.grid(column=0, row=2)
botao.configure(bg='Red')

botao_jogo = Button(janela, text="Play", command=lambda: DinoGamer.USEREVENT)
botao_jogo.grid(column=1, row=2)
botao_jogo.configure(bg="pink")

janela.mainloop()

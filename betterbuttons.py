# Imports Necessários.
import tkinter
from tkinter import Canvas, Button, PhotoImage
import os


# Criando a Classe de Programa.
class Programa:
    # Função principal.
    def __init__(self, root):
        # Função para Colocar ele Inteiramente Vermelho.
        def desligar_anim_on(event):
            self.botao_desligar_anim.config(image=self.img_desligar_selec)

        # Função para Colocar ele no Padrão.
        def desligar_anim_off(event):
            self.botao_desligar_anim.config(image=self.img_desligar)

        # Função para Colocar ele Inteiramente Verde.
        def confirmar_anim_on(event):
            self.botao_confirmar_anim.config(image=self.img_confirmar_selec)

        # Função para Colocar ele no Padrão.
        def confirmar_anim_off(event):
            self.botao_confirmar_anim.config(image=self.img_confirmar)

        # Função para Colocar ele Inteiramente Azul.
        def cancelar_anim_on(event):
            self.botao_cancelar_anim.config(image=self.img_cancelar_selec)

        # Função para Colocar ele no Padrão.
        def cancelar_anim_off(event):
            self.botao_cancelar_anim.config(image=self.img_cancelar)

        # Caminho das Imagens.
        self.dirname = os.path.dirname(__file__)

        # Botão de Desligar.
        self.img_desligar = PhotoImage(
            file=f'{self.dirname}\\Imagens\\botao-desligar.png')
        self.botao_desligar = Button(root,
                                     highlightcolor='#FF0000',
                                     borderwidth=0,
                                     bg='#191919',
                                     activebackground='#191919',
                                     relief='flat',
                                     image=self.img_desligar,
                                     command=lambda: print('Desligar'))
        self.botao_desligar.place(x=90.5, y=76)

        # Botão de Desligar Animado.
        self.botao_desligar_anim = Button(root,
                                          highlightcolor='#FF0000',
                                          borderwidth=0,
                                          bg='#191919',
                                          activebackground='#191919',
                                          relief='flat',
                                          image=self.img_desligar,
                                          command=lambda: print('Desligar Animado'))
        self.botao_desligar_anim.place(x=240.5, y=76)
        self.botao_desligar_anim.bind('<Enter>', desligar_anim_on)
        self.botao_desligar_anim.bind('<Leave>', desligar_anim_off)

        # Botão de Desligar Selecionado.
        self.img_desligar_selec = PhotoImage(
            file=f'{self.dirname}\\Imagens\\botao-desligar-selec.png')
        self.botao_desligar_selec = Button(root,
                                           highlightcolor='#FF0000',
                                           borderwidth=0,
                                           bg='#191919',
                                           activebackground='#191919',
                                           relief='flat',
                                           image=self.img_desligar_selec,
                                           command=lambda: print('Desligar Selecionado'))
        self.botao_desligar_selec.place(x=390.5, y=76)

        # Botão de Confirmar.
        self.img_confirmar = PhotoImage(
            file=f'{self.dirname}\\Imagens\\botao-confirmar.png')
        self.botao_confirmar = Button(root,
                                      highlightcolor='#FF0000',
                                      borderwidth=0,
                                      bg='#191919',
                                      activebackground='#191919',
                                      relief='flat',
                                      image=self.img_confirmar,
                                      command=lambda: print('Confirmar'))
        self.botao_confirmar.place(x=90.5, y=176)

        # Botão de Confirmar Animado.
        self.botao_confirmar_anim = Button(root,
                                           highlightcolor='#FF0000',
                                           borderwidth=0,
                                           bg='#191919',
                                           activebackground='#191919',
                                           relief='flat',
                                           image=self.img_confirmar,
                                           command=lambda: print('Confirmar Animado'))
        self.botao_confirmar_anim.place(x=240.5, y=176)
        self.botao_confirmar_anim.bind('<Enter>', confirmar_anim_on)
        self.botao_confirmar_anim.bind('<Leave>', confirmar_anim_off)

        # Botão de Confirmar Selecionado.
        self.img_confirmar_selec = PhotoImage(
            file=f'{self.dirname}\\Imagens\\botao-confirmar-selec.png')
        self.botao_confirmar_selec = Button(root,
                                            highlightcolor='#FF0000',
                                            borderwidth=0,
                                            bg='#191919',
                                            activebackground='#191919',
                                            relief='flat',
                                            image=self.img_confirmar_selec,
                                            command=lambda: print('Confirmar Selecionado'))
        self.botao_confirmar_selec.place(x=390.5, y=176)

        # Botão de Cancelar.
        self.img_cancelar = PhotoImage(
            file=f'{self.dirname}\\Imagens\\botao-cancelar.png')
        self.botao_cancelar = Button(root,
                                     highlightcolor='#FF0000',
                                     borderwidth=0,
                                     bg='#191919',
                                     activebackground='#191919',
                                     relief='flat',
                                     image=self.img_cancelar,
                                     command=lambda: print('Cancelar'))
        self.botao_cancelar.place(x=90.5, y=276)

        # Botão de Cancelar Animado.
        self.botao_cancelar_anim = Button(root,
                                          highlightcolor='#FF0000',
                                          borderwidth=0,
                                          bg='#191919',
                                          activebackground='#191919',
                                          relief='flat',
                                          image=self.img_cancelar,
                                          command=lambda: print('Cancelar Animado'))
        self.botao_cancelar_anim.place(x=240.5, y=276)
        self.botao_cancelar_anim.bind('<Enter>', cancelar_anim_on)
        self.botao_cancelar_anim.bind('<Leave>', cancelar_anim_off)

        # Botão de Cancelar Selecionado.
        self.img_cancelar_selec = PhotoImage(
            file=f'{self.dirname}\\Imagens\\botao-cancelar-selec.png')
        self.botao_cancelar_selec = Button(root,
                                           highlightcolor='#FF0000',
                                           borderwidth=0,
                                           bg='#191919',
                                           activebackground='#191919',
                                           relief='flat',
                                           image=self.img_cancelar_selec,
                                           command=lambda: print('Cancelar Selecionado'))
        self.botao_cancelar_selec.place(x=390.5, y=276)


# Para iniciar o TKinter.
root = tkinter.Tk()

# Colocar o título da janela.
root.title('Buttons')

# Fazer com que não dê para alterar o tamanho da tela.
root.resizable(width=False, height=False)

# Tela do Programa.
tela_canvas = Canvas(root, width=600,
                     height=400,
                     bg='#191919',
                     relief='flat')
tela_canvas.pack()

# Função para apenas executar se for o programa principal.
if __name__ == '__main__':
    App = Programa(root)
    root.mainloop()

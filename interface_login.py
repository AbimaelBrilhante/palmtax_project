from tkinter import *
from Interface import Application

class Application_login:
    def __init__(self, master=""):
        self.fontePadrao = ("Verdana", "8","bold")
        self.conteiner1 = Frame(master)
        self.conteiner1["pady"] = 10
        self.conteiner1.pack()
        self.conteiner1.configure(bg='#333333')

        self.conteiner2 = Frame(master)
        self.conteiner2["padx"] = 20
        self.conteiner2["pady"] = 8
        self.conteiner2.pack()
        self.conteiner2.configure(bg='#333333')

        self.conteiner3 = Frame(master)
        self.conteiner3["padx"] = 20
        self.conteiner3.pack()
        self.conteiner3.configure(bg='#333333')

        self.conteiner4 = Frame(master)
        self.conteiner4["pady"] = 20
        self.conteiner4.pack()
        self.conteiner4.configure(bg='#333333')

        self.titulo = Label(self.conteiner1, text="Dados do usuário")
        self.titulo["font"] = ("Verdana", "8", "bold")
        self.titulo.pack()
        self.titulo.configure(bg='#333333', foreground='white')


        self.nomeLabel = Label(self.conteiner2,text="Usuário", font=self.fontePadrao)
        self.nomeLabel["padx"] = 10
        self.nomeLabel.pack(side=LEFT)
        self.nomeLabel.configure(bg='#333333',foreground='white')

        self.nome = Entry(self.conteiner2)
        self.nome["width"] = 15
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.conteiner3, text="Senha", font=self.fontePadrao)
        self.senhaLabel["padx"] = 15
        self.senhaLabel.pack(side=LEFT)
        self.senhaLabel.configure(bg='#333333',foreground='white')

        self.senha = Entry(self.conteiner3)
        self.senha["width"] = 15
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.conteiner4)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Verdana", "8","bold")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
        self.autenticar.configure(bg='#4c4c4c', foreground='white')

        self.mensagem = Label(self.conteiner4, text="", font=self.fontePadrao)
        self.mensagem.pack()
        self.mensagem.configure(bg='#333333', foreground='#FA8072',pady=10)


    def verificaSenha(self):

        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "admin" and senha == "admin":
            self.conteiner1.pack_forget()
            self.conteiner2.pack_forget()
            self.conteiner3.pack_forget()
            self.conteiner4.pack_forget()
            self.mensagem["text"] = Application()

        else:
            self.mensagem["text"] = "Erro na autenticação"

if __name__ == "__main__":
    root_login = Tk()
    root_login.title('PalmTax')
    root_login.configure(bg='#333333')
    Application_login(root_login)
    root_login.mainloop()

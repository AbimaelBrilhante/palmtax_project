from Consultas import consultas
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8","bold")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container1.configure(bg='#333333')
        self.container2 = Frame(master)
        self.container2["padx"] = 80
        self.container2["pady"] = 5
        self.container2.pack()
        self.container2.configure(bg='#333333')
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container3.configure(bg='#333333')
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container4.configure(bg='#333333')
        self.container5 = Frame(master)
        self.container5["padx"] = 100
        self.container5["pady"] = 5
        self.container5.pack()
        self.container5.configure(bg='#333333')
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container6.configure(bg='#333333')
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container7.configure(bg='#333333')
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container8.configure(bg='#333333')
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container9.configure(bg='#333333')
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container10.configure(bg='#333333')
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()
        self.container11.configure(bg='#333333')
        self.container12 = Frame(master)
        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.pack()
        self.container12.configure(bg='#333333')
        self.container13 = Frame(master)
        self.container13["padx"] = 20
        self.container13["pady"] = 5
        self.container13.pack()
        self.container13.configure(bg='#333333')
        self.container14 = Frame(master)
        self.container14["padx"] = 20
        self.container14["pady"] = 10
        self.container14.pack()
        self.container14.configure(bg='#333333')
        self.container15 = Frame(master)
        self.container15["pady"] = 15
        self.container15.pack()
        self.container15.configure(bg='#333333')

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo.pack ()
        self.titulo.configure(bg='#333333',foreground='white')

        self.lbluf = Label(self.container2,
        text="UF:", font=self.fonte, width=20)
        self.lbluf.pack(side=LEFT)

        self.txtuf = Entry(self.container2)
        self.txtuf["width"] = 18
        self.txtuf["font"] = self.fonte
        self.txtuf.pack(side=LEFT)
        self.txtuf.configure(bg='#333333', foreground='white')

        self.lblcnpjcpf = Label(self.container3,
        text="Código do Material:", font=self.fonte, width=20)
        self.lblcnpjcpf.pack(side=LEFT)

        self.txtcnpjcpf = Entry(self.container3)
        self.txtcnpjcpf["width"] = 18
        self.txtcnpjcpf["font"] = self.fonte
        self.txtcnpjcpf.pack(side=LEFT)
        self.txtcnpjcpf.configure(bg='#333333', foreground='white')


        self.lblcnpjcpf = Label(self.container4,
        text="Palavra Chave:", font=self.fonte, width=20)
        self.lblcnpjcpf.pack(side=LEFT)

        self.txtcnpjcpf = Entry(self.container4)
        self.txtcnpjcpf["width"] = 18
        self.txtcnpjcpf["font"] = self.fonte
        self.txtcnpjcpf.pack(side=LEFT)
        self.lblcnpjcpf.configure(bg='#333333', foreground='white')


        self.lblcnpjcpf = Label(self.container5,
        text="Segmento:", font=self.fonte, width=20)
        self.lblcnpjcpf.pack(side=LEFT)

        self.txtcnpjcpf = Entry(self.container5)
        self.txtcnpjcpf["width"] = 18
        self.txtcnpjcpf["font"] = self.fonte
        self.txtcnpjcpf.pack(side=LEFT)
        self.lblcnpjcpf.configure(bg='#333333', foreground='white')


        self.lblcnpjcpf = Label(self.container6,
        text="NCM:", font=self.fonte, width=20)
        self.lblcnpjcpf.pack(side=LEFT)

        self.txtcnpjcpf = Entry(self.container6)
        self.txtcnpjcpf["width"] = 18
        self.txtcnpjcpf["font"] = self.fonte
        self.txtcnpjcpf.pack(side=LEFT)
        self.lblcnpjcpf.configure(bg='#333333', foreground='white')


        self.lblcnpjcpf = Label(self.container7,
        text="Tributação:", font=self.fonte, width=20)
        self.lblcnpjcpf.pack(side=LEFT)

        self.txtcnpjcpf = Entry(self.container7)
        self.txtcnpjcpf["width"] = 18
        self.txtcnpjcpf["font"] = self.fonte
        self.txtcnpjcpf.pack(side=LEFT)



        self.bntAlterar = Button(self.container12, text="Consultar dados",
        font=self.fonte, width=15,bg='#4c4c4c', foreground='white')
        self.bntAlterar["command"] = self.consultar_dados()
        self.bntAlterar.pack (side=LEFT)

        self.bntInsert = Button(self.container12, text="Importar dados",
        font=self.fonte, width=15,bg='#4c4c4c', foreground='white')
        self.bntInsert["command"] = self.importar_dados()
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container12, text="Exportar dados",
        font=self.fonte, width=15,bg='#4c4c4c', foreground='white')
        self.bntAlterar["command"] = self.exportar_dados()
        self.bntAlterar.pack (side=LEFT)

        self.lblmsg = Label(self.container13, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        self.lblmsg.configure(bg='#333333', foreground='white')

        self.lblcnpjcpf.configure(bg='#333333', foreground='white')



    def importar_dados(self):

        pass

    def exportar_dados(self):
        pass

    def consultar_dados(self):
        user = consultas()
        user.uf = self.txtuf.get()
        print(user.uf)
        print(self.txtuf.get())




root = Tk()
frame = Frame()
root.title('PalmTax')
root.configure(bg='#333333')
frame.pack(expand=True, fill=BOTH)
Application(root)
root.mainloop()

Application.consultar_dados("self")
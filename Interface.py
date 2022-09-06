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
        self.txtuf.configure(bg='#bfbbbb', foreground='black')
        self.lbluf.configure(bg='#333333', foreground='white')

        self.lblcodigomaterial = Label(self.container3,
        text="Código do Material:", font=self.fonte, width=20)
        self.lblcodigomaterial.pack(side=LEFT)

        self.txtcodigomaterial = Entry(self.container3)
        self.txtcodigomaterial["width"] = 18
        self.txtcodigomaterial["font"] = self.fonte
        self.txtcodigomaterial.pack(side=LEFT)
        self.txtcodigomaterial.configure(bg='#bfbbbb', foreground='black')
        self.lblcodigomaterial.configure(bg='#333333', foreground='white')

        self.lblpalavrachave = Label(self.container4,
        text="Palavra Chave:", font=self.fonte, width=20)
        self.lblpalavrachave.pack(side=LEFT)

        self.txtpalavrachave = Entry(self.container4)
        self.txtpalavrachave["width"] = 18
        self.txtpalavrachave["font"] = self.fonte
        self.txtpalavrachave.pack(side=LEFT)
        self.lblpalavrachave.configure(bg='#333333', foreground='white')
        self.txtpalavrachave.configure(bg='#bfbbbb', foreground='black')


        self.lblsegmento = Label(self.container5,
        text="Segmento:", font=self.fonte, width=20)
        self.lblsegmento.pack(side=LEFT)

        self.txtsegmento = Entry(self.container5)
        self.txtsegmento["width"] = 18
        self.txtsegmento["font"] = self.fonte
        self.txtsegmento.pack(side=LEFT)
        self.lblsegmento.configure(bg='#333333', foreground='white')
        self.txtsegmento.configure(bg='#bfbbbb', foreground='black')


        self.lblncm = Label(self.container6,
        text="NCM:", font=self.fonte, width=20)
        self.lblncm.pack(side=LEFT)

        self.txtncm = Entry(self.container6)
        self.txtncm["width"] = 18
        self.txtncm["font"] = self.fonte
        self.txtncm.pack(side=LEFT)
        self.lblncm.configure(bg='#333333', foreground='white')
        self.txtncm.configure(bg='#bfbbbb', foreground='black')


        self.lbltributacao = Label(self.container7,
        text="Tributação:", font=self.fonte, width=20)
        self.lbltributacao.pack(side=LEFT)

        self.txttributacao = Entry(self.container7)
        self.txttributacao["width"] = 18
        self.txttributacao["font"] = self.fonte
        self.txttributacao.pack(side=LEFT)
        self.txttributacao.configure(bg='#bfbbbb', foreground='black')
        self.lbltributacao.configure(bg='#333333', foreground='white')



        self.bntConsultar = Button(self.container12, text="Consultar dados",
        font=self.fonte, width=15,bg='#4c4c4c', foreground='white')
        self.bntConsultar["command"] = self.consultar_dados
        self.bntConsultar.pack (side=LEFT)

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

        self.lblresposta1 = Label(self.container14,width=80, height=5)
        self.lblresposta1.pack()
        self.txtresposta1 = Entry(self.container14)
        self.txtresposta1.configure(bg='#bfbbbb', foreground='black')

        self.scroll_bar = Scrollbar(self.lblresposta1)
        self.scroll_bar.pack(side=RIGHT,fill=Y)
        self.mylist = Listbox(self.lblresposta1,yscrollcommand=self.scroll_bar.set,width=80)
        self.mylist.pack(side=LEFT, fill=BOTH)
        self.scroll_bar.config(command=self.mylist.yview)
        root.mainloop()




    def importar_dados(self):

        pass

    def exportar_dados(self):
        pass

    def consultar_dados(self):

        con = StringVar
        l_cliente1 = Label(self.mylist, textvariable=con)
        l_cliente1.grid(row=10, column=10)

        uf = (self.txtuf.get())
        codigomaterial = (self.txtcodigomaterial.get())
        palavrachave = (self.txtpalavrachave.get())
        segmento = (self.txtsegmento.get())
        ncm = (self.txtncm.get())
        tributacao = (self.txttributacao.get())


        cone = consultas.selectMaterial("self", uf, codigomaterial, palavrachave, segmento,"", ncm, tributacao)
        con.set(cone)









root = Tk()
frame = Frame()
root.title('PalmTax')
root.configure(bg='#333333')
frame.pack(expand=True, fill=BOTH)
Application(root)
root.mainloop()




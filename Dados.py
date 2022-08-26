import sqlite3

class Dados():

    def __init__(self):
        self.conexao = sqlite3.connect('palm_tax.db')
        #self.createTable()

    # def createTable(self):
    #     c = self.conexao.cursor()
    #
    #     c.execute("""create table if not exists base_tributaria (
    #         "UF" TEXT,
    #         "MATERIAL" INTEGER,
    #         "DESCRICAO_MATERIAL" TEXT,
    #         "SEG" TEXT,
    #         "GRUPO_MERCADORIAS" TEXT,
    #         "ORIGEM" INTEGER,
    #         "NCM" TEXT,
    #         "CEST" TEXT,
    #         "TRIBUTACAO" TEXT,
    #         "ALIQ_INT" TEXT,
    #         "Red_BC" TEXT,
    #         "MVA_PRATIC" TEXT,
    #         ))""")
    #     self.conexao.commit()
    #     c.close()


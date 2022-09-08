from Dados import Dados
import os


class consultas(object):


    def __init__(self, uf = "", material = "",descricao_material = "",seg = "",grupo_mercadorias = "",
                 origem = "",ncm = "",cest="",tributacao = "", aliq_int = "",red_bc = "",mva_pratic=""):
      self.info = {}
      self.uf = uf
      self.material = material
      self.descricao_material = descricao_material
      self.seg = seg
      self.grupo_mercadorias = grupo_mercadorias
      self.origem  = origem
      self.ncm = ncm
      self.cest = cest
      self.tributacao = tributacao
      self.aliq_int = aliq_int
      self.red_bc = red_bc
      self.mva_pratic = mva_pratic



    def insertProduct(self):

      banco = Dados()
      try:

          c = banco.conexao.cursor()

          c.execute("insert into base_tributaria (uf, material, descricao_material, seg, grupo_mercadorias, origem, ncm,"
                    " cest, tributacao, aliq_int, red_bc,mva_pratic) "f"values('{str(self.uf)}',"
                    f" {self.material},{self.descricao_material}, {self.seg},{self.grupo_mercadorias},{self.origem}, {self.ncm},"
                    f" {self.cest}, {self.tributacao}, {self.aliq_int}, {self.red_bc}, {self.mva_pratic} )")

          banco.conexao.commit()
          c.close()

          return "Material cadastrado com sucesso!"
      except:

          return "Ocorreu um erro na inserção do material"

    def updateUser(self):

      banco = Dados()
      try:

          c = banco.conexao.cursor()

          c.execute("update clientes set nome = '" + self.nome + "',cep = '" + self.cep + "',endereco = '" + self.endereco +
                    "',numero = '" + self.numero + "',complemento = '" + self.complemento + "',bairro = '" + self.bairro + "',cidade = '" + self.cidade + "', estado = '"
                    + self.estado +"', telefone = '" + self.telefone + "', email = '" + self.email +
                    "' where cnpjcpf = " + self.cnpjcpf + " ")

          banco.conexao.commit()
          c.close()

          return "Usuário atualizado com sucesso!"
      except:
          return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

      banco = Dados()
      try:

          c = banco.conexao.cursor()

          c.execute("delete from clientes where cnpjcpf = " + str(self.cnpjcpf) + " ")

          banco.conexao.commit()
          c.close()

          return "Usuário excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do usuário"

    def selectMaterial(self, uf = "*",material = "*",descricao_material="*",seg="*",grupo_mercadorias="*",ncm="*",tributacao="*"):
        #os.system('cls') or None
        banco = Dados()
        c = banco.conexao.cursor()
        c.execute(f"select * from base_tributaria where "
                  f"UF like '%{uf}%' AND "
                  f"MATERIAL LIKE '%{material}%' AND "
                  f"DESCRIÇÃO_MATERIAL like '%{str(descricao_material)}%' AND "
                  f"SEG LIKE '%{seg}%' AND "
                  f"GRUPO_MERCADORIAS like '%{grupo_mercadorias}%' AND "
                  f"NCM like '%{ncm}%' AND "
                  f"TRIBUTAÇÃO like '%{tributacao}%'")
#'("UF","CÓDIGO DO MATERIAL","DESCRIÇÃO DO MATERIAL","SEGMENTO","GRUPO DE MERCADORIAS","NCM","TRIBUTAÇÃO")'
        resposta = []
        for linha in c.fetchall():
            linha = str(linha[0] +" | "+ linha[1]+" | "+linha[3] +" | "+linha[6]+" | "+str(linha[8]))
            resposta.append(linha)
        return(resposta)








        c.close()


#con = consultas.selectMaterial("self","","","","","","","")



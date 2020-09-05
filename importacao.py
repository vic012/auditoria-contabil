import pandas as pd
import xlrd
import re

class Importacao:
    def __init__(self):
        #-------------------------------------------------------
        #Pega do usuario o valor do número do fornecedor
        self.fornecedor = input("Qual o fornecedor que você deseja auditar? ")
        #Importações, a planilha é antiga, por isso o xlrd
        self.book = xlrd.open_workbook("razao.xls", encoding_override='cp1252') 
        #Transformando em DataFrame
        self.arquivo = pd.read_excel(self.book)
        self.arquivo.drop(['codi_emp', 'clasc', 'nomec', 'tipo', 'numelan',
            'saldoant', 'contrap', 'ordem_nat_cta', 'origem', 'saldo',
            'mascara', 'mascrel', 'zebra1', 'tipo_lan',
            'emissao', 'codi_lote', 'nome_fantasia_incorporacao', 'nro_quebra_incorporacao',
            'natureza', 'filial', 'codigo_scp', 'descricao_scp', 'ordem'], inplace=True, axis=1)
        #Ficam apenas as colunas "codic", "datalan", "valdeb", "valcre", "historico"
        #Receberá os Números das Notas fiscais
        self.historico_separado = list()
        #-------------------------------------------------------
        
    #-------------------------------------------------------
    #Excluindo colunas desnecessárias
    def arquivoDataFrame(self):
        #Faz um loop em cada relatório, para retirar os Números das nf's
        #-------------------------------------------------------
        for historico in self.arquivo['historico']:
            historicoSeparado = list()
            filtro = re.findall('([0-9]+)',historico)

            if (len(filtro) != 0):
                historicoSeparado.append(filtro)
            else:
                pass

            if (len(historicoSeparado) != 0):
                self.historico_separado.append(historicoSeparado[0])
            else:
                self.historico_separado.append("Lançamento sem número de NF")

        #Adiciona o número separado no dataframe
        df_historicos = pd.DataFrame(self.historico_separado)
        self.arquivo['historico sep'] = df_historicos
        #-------------------------------------------------------

        compras = self.arquivo.loc[(self.arquivo['valcre'] != 0) & (self.arquivo['codic'] == int(self.fornecedor))]
        pagamentos = self.arquivo.loc[(self.arquivo['valdeb'] != 0) & (self.arquivo['codic'] == int(self.fornecedor))]
        saldo_anterior = self.arquivo.loc[(self.arquivo['valdeb'] == 0) & (self.arquivo['valcre'] == 0) & (self.arquivo['codic'] == int(self.fornecedor))]
        #Para teste utilize----------------------------------------------
        #compras.to_excel('compras.xlsx') 
        #pagamentos.to_excel('Pagamentos.xlsx')
        #saldo_anterior.to_excel('Saldos.xlsx')
        print(saldo_anterior.head(10))
                
teste = Importacao()
teste.arquivoDataFrame()
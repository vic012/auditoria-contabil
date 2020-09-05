import pandas as pd
import xlrd

class Importacao:
    def __init__(self):
        #-------------------------------------------------------
        #Pega do usuario o valor do número do fornecedor
        self.fornecedor = input("Qual o fornecedor que você deseja auditar? ")
        #Importações, a planilha é antiga, por isso o xlrd
        self.book = xlrd.open_workbook("razao.xls", encoding_override='cp1252') 
        #Transformando em DataFrame
        self.arquivo = pd.read_excel(self.book)
        #-------------------------------------------------------

    #-------------------------------------------------------
    #Excluindo colunas desnecessárias
    def arquivoDataFrame(self):
        self.arquivo.drop(['codi_emp', 'clasc', 'tipo', 'numelan',
            'saldoant', 'contrap', 'ordem_nat_cta', 'origem', 'saldo',
            'mascara', 'mascrel', 'zebra1', 'tipo_lan',
            'emissao', 'codi_lote', 'nome_fantasia_incorporacao', 'nro_quebra_incorporacao',
            'natureza', 'filial', 'codigo_scp', 'descricao_scp', 'ordem'], inplace=True, axis=1)
        #Ficam apenas as colunas "nomec", "codic", "datalan", "valdeb", "valcre", "historico"
        compras = self.arquivo.loc[(self.arquivo['valcre'] != 0) & (self.arquivo['codic'] == int(self.fornecedor))]
        pagamentos = self.arquivo.loc[(self.arquivo['valdeb'] != 0) & (self.arquivo['codic'] == int(self.fornecedor))]
        saldo_anterior = self.arquivo.loc[(self.arquivo['valdeb'] == 0) & (self.arquivo['valcre'] == 0) & (self.arquivo['codic'] == int(self.fornecedor))]
        
        #Para teste utilize----------------------------------------------
        #compras.to_excel('compras.xlsx') 
        #pagamentos.to_excel('Pagamentos.xlsx')
        #saldo_anterior.to_excel('Saldos.xlsx')


        
teste = Importacao()
teste.arquivoDataFrame()
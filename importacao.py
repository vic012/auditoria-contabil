import pandas as pd
import xlrd 

class Importacao:
    def __init__(self):
        #-------------------------------------------------------
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
        compras = self.arquivo.loc[self.arquivo['valcre'] != 0]
        pagamentos = self.arquivo.loc[self.arquivo['valdeb'] != 0]
        saldos_anteriores = self.arquivo.loc[(self.arquivo['valdeb'] == 0) & (self.arquivo['valcre'] == 0)]
        
teste = Importacao()
teste.arquivoDataFrame()
import pandas as pd
import xlrd 

#-------------------------------------------------------
#Importações, a planilha é antiga, por isso o xlrd
book = xlrd.open_workbook("jucelio.xls", encoding_override='cp1252') 
#Transformando em DataFrame
arquivo = pd.read_excel(book)
#-------------------------------------------------------

#-------------------------------------------------------
#Excluindo colunas desnecessárias
arquivo.drop(['codi_emp', 'clasc', 'codic', 'tipo', 'numelan',
    'saldoant', 'contrap', 'ordem_nat_cta', 'origem', 'saldo',
    'saldo_exe', 'mascara', 'mascrel', 'zebra1', 'tipo_lan',
    'emissao', 'codi_lote', 'nome_fantasia_incorporacao', 'nro_quebra_incorporacao',
    'natureza', 'filial', 'codigo_scp', 'descricao_scp', 'ordem'], inplace=True, axis=1)
#Ficam apenas as colunas "nomec", "datalan", "valdeb", "valcre", "historico"
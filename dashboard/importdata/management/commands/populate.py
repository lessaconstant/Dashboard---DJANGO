import os
from django.core.management.base import BaseCommand
from importdata.models import Dados
from django.conf import settings
import pandas as pd
import numpy as np

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando o processo de população do banco de dados...'))
        
        # Caminho estático para o arquivo CSV
        caminho = os.path.join(os.getcwd(), 'importdata', 'static', 'data', 'MICRODADOS_ENEM_2022.csv')

        # Verificar se o arquivo CSV existe
        if not os.path.exists(caminho):
            self.stdout.write(self.style.ERROR('Arquivo CSV não encontrado. Certifique-se de que o caminho está correto.'))
            return

        try:
            # Ler o CSV e realizar manipulações necessárias
            colunas = ['NU_INSCRICAO', 'TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA',
                       'TP_NACIONALIDADE', 'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU', 'TP_ESCOLA', 'TP_ENSINO',
                       'IN_TREINEIRO', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

            dados = pd.read_csv(caminho, encoding="ISO-8859-1", sep=";", usecols=colunas,
                    na_values=['NA', 'N/A'],  # Define quais valores devem ser considerados como NA (não disponível)
                    dtype={'NU_NOTA_CN': 'float64', 'NU_NOTA_CH': 'float64',  # Define os tipos de dados para essas colunas
                           'NU_NOTA_LC': 'float64', 'NU_NOTA_MT': 'float64', 'NU_NOTA_REDACAO': 'float64'})


            # Dividir os dados em lotes
            num_lotes = 50  # Defina o número de lotes desejado
            lotes = np.array_split(dados, num_lotes)

            for lote in lotes[0:1]:
                df = lote
                df['media'] = ((df.NU_NOTA_CN + df.NU_NOTA_CH + df.NU_NOTA_LC + df.NU_NOTA_MT + df.NU_NOTA_REDACAO) / 5)

                df = df.fillna(0)
                df['IN_TREINEIRO'] = df['IN_TREINEIRO'].astype(bool)
                df['TP_ENSINO'] = df['TP_ENSINO'].astype(int)
                df[df.columns[0:11]] = df[df.columns[0:11]].astype(str)
                df['NU_INSCRICAO'] = df['NU_INSCRICAO'].astype(str)
                df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']] = df[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].round(2)  # Arredonda para 2 casas decimais

                df.columns = ['inscricao', 'faixa_idade', 'sexo', 'estado_civil', 'raca', 'nacionalidade',
                              'conclusao_status', 'conclusao_ano', 'tipo_escola', 'conclusao_situacao',
                              'treineiro', 'CN', 'CH', 'LC', 'MT', 'REDACAO', 'MEDIA']

                # Fim manipulação

                dataframe_data = df.to_dict(orient="records")  # Formatar as linhas para dicionarios
                
                # Criar instâncias do modelo Dados a inseri-las no banco
                instances = [Dados(**data) for data in dataframe_data]

                Dados.objects.bulk_create(instances)

            self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ocorreu um erro durante a execução do comando: {e}"))

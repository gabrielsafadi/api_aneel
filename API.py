import requests
import pandas as pd
from google.cloud import bigquery
import os
from datetime import datetime
from google.oauth2 import service_account

class API_ANEEL: 

    def __init__(self, base_url, resource_id, limit_per_page, project_id, dataset_id, table_id):
        # URL base da API
        self.base_url = base_url
        # ID do recurso (substitua pelo seu ID de recurso)
        self.resource_id = resource_id
        # Número máximo de resultados por página (definir o limite máximo)
        self.limit_per_page = limit_per_page
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id

        

    def get_data(self, df):


        # Inicializa uma lista para armazenar todos os dados
        all_data = []

        # Inicializa o parâmetro de offset para a primeira página
        offset = 0

        while True:
            # Parâmetros da requisição
            params = {
                "resource_id": self.resource_id,
                "limit": self.limit_per_page,
                "offset": offset,
                "q": "EQUATORIAL ALAGOAS DISTRIBUIDORA DE ENERGIA S.A."
            }

            # Faz a requisição à API
            response = requests.get(self.base_url, params=params)

            # Nesse trecho ocorre o processo de paginação, tendo em vista que as páginas são limitadas a 32000 registros
            if response.status_code == 200:
                data = response.json()
                records = data['result']['records']
        
                # Adiciona os registros da página à lista de todos os dados
                all_data.extend(records)
        
                # Verifica se há mais páginas
                if len(records) < self.limit_per_page:
                    break  # Sai do loop se não houver mais páginas
                else:
                    offset += self.limit_per_page  # Avança para a próxima página
            else:
                print("Falha na requisição:", response.status_code)
                break

        # Cria um DataFrame com todos os dados
        self.df = pd.DataFrame(all_data)

        # Insere uma coluna chamada DataCarregamento com a data atual

        self.df['DataCarregamento'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Retorna dados do dataframe
        self.df

    
    def load_data(self):
        # Substitua pelo caminho para o seu arquivo de credenciais JSON
        credentials_path = "gcp-credentials.json"

        # Configura as credenciais
        client = bigquery.Client.from_service_account_json(credentials_path)

        # Insere os dados no BigQuery
        table_ref = client.dataset(self.dataset_id).table(self.table_id)
        job_config = bigquery.LoadJobConfig(write_disposition='WRITE_TRUNCATE', autodetect=True)
        job = client.load_table_from_dataframe(self.df, table_ref, job_config=job_config)
        job.result()  # Aguarda a conclusão do job

        return(f'Dados inseridos com sucesso na tabela {self.table_id}')

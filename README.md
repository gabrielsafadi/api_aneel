# Extração e inserção de dados Interrupções de Energia Elétrica (ANEEL)

O Analisador de Interrupções de Energia Elétrica é uma ferramenta que permite extrair dados da API da ANEEL para análise de indicadores de interrupções de energia elétrica. 
Este projeto foi desenvolvido no ambiente do Google Cloud Platform (GCP) e utiliza as Cloud Functions e o BigQuery para processar e armazenar os dados. Seu "ponto final" é no Power BI, onde serão criadas análises baseadas nos dados extraídos e disponibilizados
publicamente.

## Visão Geral

Este projeto tem como objetivo facilitar a análise de indicadores de interrupções de energia elétrica fornecidos pela Agência Nacional de Energia Elétrica (ANEEL). 
Ele permite extrair esses dados da API da ANEEL, processá-los e inseri-los em uma tabela do BigQuery para posterior análise e geração de relatórios.

## Requisitos

Para usar este projeto, você precisará:

- Baixar as credenciais da Service Account gerada no IAM do GCP e salvar o arquivo JSON com o nome de "gcp-credentials.json".
- Alterar as informações de `resource_id` para corresponder ao conjunto de dados da ANEEL desejado. Você pode encontrar os recursos disponíveis em [dadosabertos.aneel.gov.br](https://dadosabertos.aneel.gov.br/organization/agencia-nacional-de-energia-eletrica).
- Configurar as informações de tabela, projeto e outras configurações do BigQuery de acordo com suas necessidades.

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/gabrielsafadi/api_aneel.git
   
2. Configure o arquivo gcp-credentials.json com as credenciais da Service Account do GCP.

3. Personalize as informações de resource_id, tabela, projeto, e outras configurações no código, conforme necessário.

4. Execute o código para iniciar a extração e inserção de dados no BigQuery.

5. Exemplo de requisição para a Cloud Function (Para Authorization, utilizar a private_key presente nas credenciais ou gerar Bearer):  {
     "base_url": "",
     "resource_id": "",
     "limit_per_page": 0,
     "project_id": "",
     "dataset_id": "",
     "table_id": ""
 }

## Reaproveitamento
Este código pode ser facilmente adaptado para extrair e analisar outros conjuntos de dados disponíveis no site da ANEEL. Basta modificar o resource_id correspondente e as configurações do BigQuery para atender às suas necessidades.

## Contribuição
Se você deseja contribuir para este projeto, sinta-se à vontade para abrir issues, enviar solicitações de pull ou propor melhorias. Sua colaboração é bem-vinda!

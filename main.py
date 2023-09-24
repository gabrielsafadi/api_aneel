import requests
from API.API import API_ANEEL

def main(request):
    # requisições
    request_json = request.get_json()

    base_url = request_json['base_url']
    resource_id = request_json['resource_id']
    limit_per_page = request_json['limit_per_page']
    project_id = request_json['project_id']
    dataset_id = request_json['dataset_id']
    table_id = request_json['table_id']

    instance = API_ANEEL(base_url, resource_id, limit_per_page, project_id, dataset_id, table_id)

    get_data = instance.get_data('df')

    instance.load_data()

    return 'Dados carregados com sucesso!'
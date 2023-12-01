import requests

def busca_cnpj(cnpj: str):
    url_base = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url_base)
    result = response.json()
    return result
import requests, re

def busca_cnpj(cnpj: str):
    cleaned_cnpj = re.sub(r'\D', '', cnpj)
    url_base = f"https://receitaws.com.br/v1/cnpj/{cleaned_cnpj}"
    response = requests.get(url_base)
    result = response.json()
    if result["status"] == "ERROR":
        return False      
    return result
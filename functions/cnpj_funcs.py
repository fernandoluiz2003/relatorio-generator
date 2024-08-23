import re
from typing import Union, List

def cnpj_cleaner(cnpjs: Union[List[str], str]) -> List[str] | str:
    """Remove the - , / and . from a CNPJ"""
    if isinstance(cnpjs, list):
        return [re.sub(r'\D', '', cnpj) for cnpj in cnpjs]
    return re.sub(r'\D', '', cnpjs)

def cnpj_finder(text: str) -> list:
    """Find all the CNPJs in a text"""
    return re.findall(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', text)

def get_cnpj(path: str) -> list:
    with open(path, 'r') as file:
        CNPJs = file.readlines()
    
    return CNPJs
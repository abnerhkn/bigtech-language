import requests
from config import GITHUB_URL, GITHUB_TOKEN, logger

def extract_repositories(owners):
    logger.info("Iniciando extração dos repositórios.")
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    repos_list = []
    for owner in owners:
        logger.info(f"➡️ Buscando repositórios de: {owner}")
        page = 1
        while True:
            url = f'{GITHUB_URL}/users/{owner}/repos?page={page}'
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                logger.warning(f"Erro ao buscar {owner} (status {response.status_code})")
                break
            repos = response.json()
            if not repos:
                break
            repos_list.extend(repos)
            page += 1

    logger.info(f"Total de repositórios extraídos: {len(repos_list)}")
    return repos_list

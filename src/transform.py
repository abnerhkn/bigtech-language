import pandas as pd
from datetime import datetime
from config import logger

def transform_repositories(repos_list):
    logger.info("Limpando e estruturando os dados.")

    repos_list_limpa = [
        repo for repo in repos_list
        if repo.get('language') and repo.get('name') and repo.get('description')
    ]
    logger.info(f"Repositórios após limpeza: {len(repos_list_limpa)}")

    df = pd.DataFrame({
        'bigtech_name': [repo['owner']['login'] for repo in repos_list_limpa],
        'language': [repo['language'] for repo in repos_list_limpa],
        'creation_at': [
            datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d-%m-%Y')
            for repo in repos_list_limpa
        ]
    })

    logger.info("DataFrame gerado.")
    return df

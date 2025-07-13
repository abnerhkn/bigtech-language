from datetime import datetime
from config import logger

def load_to_csv(df):
    data_hoje = datetime.today().strftime('%d-%m-%Y')
    nome_arquivo = f'bigtech_language_{data_hoje}.csv'
    df.to_csv(f'data/{nome_arquivo}', index=False)
    logger.info(f"Arquivo CSV salvo como: {nome_arquivo}")

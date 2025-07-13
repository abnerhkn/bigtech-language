from src.extract import extract_repositories
from src.transform import transform_repositories
from src.load import load_to_csv

if __name__ == '__main__':
    owners = ['google', 'microsoft', 'meta']
    repos = extract_repositories(owners)
    df = transform_repositories(repos)
    load_to_csv(df)

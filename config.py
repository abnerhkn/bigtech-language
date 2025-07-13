import os
from dotenv import load_dotenv
import logging

load_dotenv()

GITHUB_URL = os.getenv('GITHUB_URL')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)
logger = logging.getLogger(__name__)

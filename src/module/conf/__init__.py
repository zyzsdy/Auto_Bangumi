import os
from .log import setup_logger, LOG_PATH
from .config import settings, VERSION
from .const import ROOT_PATH


TMDB_API = "32b19d6a05b512190a056fa4e747cbbc"
DATA_PATH = os.path.join(ROOT_PATH, "data/data.json")

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..",".."))
DATA_DIR = os.path.join(BASE_DIR, "final_proj_data")

FILES_PATH : str = os.getenv("FILES_PATH",DATA_DIR)

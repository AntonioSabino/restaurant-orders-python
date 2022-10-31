import os


def analyze_log(path_to_file):
    if not os.path.exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

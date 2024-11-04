import pandas as pd

def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Planilha lida com sucesso.")
        return df
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
        return None

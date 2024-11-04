import pyodbc
from src.config.settings import DB_CONFIG

def connect_to_sql():
    connection_str = (
        f"DRIVER={DB_CONFIG['driver']};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']}"
    )
    try:
        conn = pyodbc.connect(connection_str)
        print("Conexão com SQL Server bem-sucedida.")
        return conn
    except Exception as e:
        print("Erro na conexão com o SQL Server:", e)
        return None

def insert_data_to_sql(df, conn):
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            '''
            INSERT INTO Produtos (Nome, Categoria, Preco, Quantidade)
            VALUES (?, ?, ?, ?)
            ''',
            row['Nome'], row['Categoria'], row['Preco'], row['Quantidade']
        )
    conn.commit()
    print("Dados inseridos com sucesso.")

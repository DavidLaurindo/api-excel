from src.db.database import connect_to_sql, insert_data_to_sql
from src.utils.data_loader import load_excel

file_path = r'C:\Users\davis\Documents\Projetos\api-excel\data\Produtos.xlsx'

# Carregar a planilha
df = load_excel(file_path)
print(df.columns)
if df is not None:
    # Conectar ao banco de dados e inserir os dados
    conn = connect_to_sql()
    if conn:
        insert_data_to_sql(df, conn)
        conn.close()

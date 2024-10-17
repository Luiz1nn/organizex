import warnings
import pandas as pd

warnings.filterwarnings("ignore", category=UserWarning)

input_file = './xlsx/file.xlsx'
output_file = './xlsx/new_file.xlsx'

df = pd.read_excel(input_file)

filter_keywords = ['Saldo Anterior', 'Saldo do dia']
df_filtered = df[~df.isin(filter_keywords).any(axis=1)]

df_final = pd.DataFrame({
    'Data': df_filtered['Data'],
    'Descrição': df_filtered['Detalhes'],
    'Categoria': '',
    'Valor': df_filtered['Valor'],
    'Situação': ''
})

df_final.to_excel(output_file, index=False)

print(f"Arquivo salvo em: {output_file}")

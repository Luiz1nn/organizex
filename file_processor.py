import pandas as pd
from pandas import DataFrame

def process_file(input_file: str, output_file: str) -> None:
    df: DataFrame = pd.read_excel(input_file)

    filter_keywords: list[str] = ['Saldo Anterior', 'Saldo do dia', 'S A L D O']
    df_filtered: DataFrame = df[~df.isin(filter_keywords).any(axis=1)]

    df_final: DataFrame = pd.DataFrame({
        'Data': df_filtered['Data'],
        'Descrição': df_filtered['Detalhes'],
        'Categoria': '',
        'Valor': df_filtered['Valor'],
        'Situação': ''
    })

    df_final.to_excel(output_file, index=False)

    print(f"Arquivo salvo em: {output_file}")
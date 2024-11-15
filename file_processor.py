import pandas as pd
from pandas import DataFrame
from utils import remove_dates, remove_sequential_numbers, remove_times, remove_extra_spaces, convert_to_xls


def process_file(input_file: str, output_file: str) -> None:
    try:
        df: DataFrame = pd.read_excel(input_file)

        filter_keywords: list[str] = ['Saldo Anterior', 'Saldo do dia', 'S A L D O']
        df_filtered: DataFrame = df[~df.isin(filter_keywords).any(axis=1)]

        df_filtered['Detalhes'] = df_filtered['Detalhes'].apply(remove_dates).apply(remove_times).apply(remove_sequential_numbers).apply(remove_extra_spaces)

        df_final: DataFrame = pd.DataFrame({
            'Data': df_filtered['Data'],
            'Descrição': df_filtered['Detalhes'],
            'Categoria': '',
            'Valor': df_filtered['Valor'],
            'Situação': ''
        })

        convert_to_xls(df_final, output_file)

        print(f"Arquivo salvo em: {output_file}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


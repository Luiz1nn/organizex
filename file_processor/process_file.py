import pandas as pd
from pandas import DataFrame
from utils import (
    normalize_text,
    remove_dates,
    remove_sequential_numbers,
    remove_times,
    remove_extra_spaces,
)
from file_processor.check_and_fill_empty_details import check_and_fill_empty_details
from file_processor.convert_to_xls import convert_to_xls
from file_processor.get_category_value_from_json import get_category_value_from_json
from file_processor.update_details_for_credit_payment import update_details_for_credit_payment


def process_file(input_file: str, output_file: str) -> None:
    try:
        df: DataFrame = pd.read_excel(input_file)

        check_and_fill_empty_details(df, 'Detalhes')

        update_details_for_credit_payment(df)

        filter_keywords: list[str] = [
            'Saldo Anterior', 'Saldo do dia', 'S A L D O'
        ]

        df_filtered: DataFrame = df[
            ~df.isin(filter_keywords).any(axis=1)
        ].copy()

        df_filtered.loc[:, 'Detalhes'] = (
            df_filtered['Detalhes']
            .apply(remove_dates)
            .apply(remove_times)
            .apply(remove_sequential_numbers)
            .apply(remove_extra_spaces)
            .apply(normalize_text)
        )

        df_filtered.loc[:, 'Categoria'] = df_filtered['Detalhes'].apply(
            get_category_value_from_json
        )

        df_final: DataFrame = pd.DataFrame({
            'Data': df_filtered['Data'],
            'Descrição': df_filtered['Detalhes'],
            'Categoria': df_filtered['Categoria'],
            'Valor': df_filtered['Valor'],
            'Situação': ''
        })

        convert_to_xls(df_final, output_file)

        print(f"Arquivo salvo em: {output_file}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

from pandas import DataFrame


def check_and_fill_empty_details(df: DataFrame, column: str) -> None:
    df[column] = (
        df[column]
        .fillna('Valor não informado')
        .replace(
            '',
            'Valor não informado'
        )
    )

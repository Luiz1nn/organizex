from pandas import DataFrame


def update_details_for_credit_payment(df: DataFrame) -> None:
    df.loc[df['Lançamento'] == 'Pagto cartão crédito',
           'Detalhes'] = 'Fatura do Cartão de Crédito'

import pandas as pd


def populate_db(path, your_model):

    dataframe = pd.read_excel(str(path))

    keys = list(dataframe.columns)

    values = dataframe.values

    for value in values:
        populate = dict(zip(keys, value))
        your_model.objects.create(**populate)
               
    """
    Valor_list retorna um lista no formato [{nome: xxx, idade: xx, aniversario: xxxx-xx-xx, id: xx},{},{}]
    """     
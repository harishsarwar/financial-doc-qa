import pandas as pd

def format_tables(tables):
    dfs = []
    for table in tables:
        df = pd.DataFrame(table[1:], columns=table[0])
        dfs.append(df)
    return dfs

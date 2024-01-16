import pandas as pd
from MappingTools.AI.Tavily import find_url


def get_data(file_path):
    df = pd.read_excel(file_path, engine="openpyxl")
    return df


def insert_urls(file_path):
    df = get_data(file_path)
    # Iterate over the DataFrame and add a value to the "קישור לאתר" column
    # For demonstration, I'll add a generic value like 'example.com'.
    # This can be replaced with the actual logic needed.
    for index, row in df.iterrows():
        print(index)
        if not pd.isna(df.at[index, 'קישור לאתר']):
            continue
        if not pd.isna(df.at[index, 'שם החברה באנגלית']):
            name = df.at[index, 'שם החברה באנגלית']
        else:
            name = df.at[index, 'שם הארגון']
        url = find_url(name, df.at[index, 'כתובת רישום'])
        print(url)
        # df.at[index, 'קישור לאתר'] = df.at[index, 'קישור לאתר']
        if url == '':
            df.at[index, 'קישור לאתר'] = 'no website'
            continue
        df.at[index, 'קישור לאתר'] = url
        print("END")

    # Write the transformed data back to an Excel file
    output_file_path = file_path
    df.to_excel(output_file_path, index=False)


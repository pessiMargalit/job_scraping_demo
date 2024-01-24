from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup

career_key_words = {"Careers", "Jobs", "Opportunities", "Vacancies", "Openings", "Positions", "Employment", "Work",
                    "Hiring", "Recruitment"
                              "קריירות", 'מקצועות', "גיוס", "תעסוקה", "משרות", "דרושים", "עבודה"}


# Karierot (קריירות)
# Avoda (עבודה)
# Misradim (משרדים)
# Hafakot (הפקות)
# Ptiha (פתיחה)
# Taasuka (תעסוקה)
# Miktsoot (מקצועות)
# Pnuyot (פנויות)
# Mismakim (משרות)
# Gיius (גיוס)
def get_career_url(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    for a in soup.findAll('a'):
        a_str = str(a)
        if any(careers in a_str for careers in career_key_words):
            a_str = str(a['href'])
            if a_str:
                if 'http' not in a_str:
                    career_url = urljoin(url, a_str)
                    return career_url

                return a_str

    # return company_english_name.text


print(get_career_url('https://www.nizat.com/'))
import pandas as pd
from mappingTools.AI.Tavily import find_url


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
        if pd.isna(df.at[index, 'קישור לאתר']):
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
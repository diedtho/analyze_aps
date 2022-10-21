import os
import re
import pandas as pd
from docx2txt import docx2txt

def file_to_text(filepath):
    print(f'filepath={filepath}')
    file_extension = re.sub(r'.*\.([^.]+)$', r'\1', filepath)
    if file_extension in ['txt', 'csv', 'log', 'md']:
        try:
            with open(filepath, 'r') as fr:
                text = fr.read()
            return text
        except:
            return ""
    elif 'docx' in file_extension:
        try:
            text = docx2txt.process(filepath)
            return text
        except:
            return ""
    elif file_extension in ['doc']:
        # implementation needed
        return ""
    else:
        return ""

def load_texts_into_corp(project_name='startfolder', data_folder='../data'):
    dir_content_df_path = os.path.join(data_folder, f'{project_name}_content.csv')
    df = pd.read_csv(dir_content_df_path, encoding='utf8', sep=';', index_col=0)
    values = ['csv', 'doc', 'docx', 'txt', 'md', 'log']
    df_files = df[df['Type'].str.contains('file')].copy(deep=True)
    print(df_files)
    first = True
    for val in values:
        if first is True:
            df_files_txt = df_files[df_files['Name'].str.match(f'.*\.{val}')].copy(deep=True)
            df_files_txt.drop('Type', axis=1, inplace=True)
            print(df_files_txt)
            df_files_txt['Fullpath'] = os.path.join(str(df_files_txt['Path']), str(df_files_txt['Name']))
            df_files_txt["Text"] = df_files_txt['Fullpath'].apply(lambda x: file_to_text(x))
            csv_path = os.path.join(f'{data_folder}', f'{project_name}_text_corpus.csv')
            df_files_txt.to_csv(csv_path, encoding='utf8', sep=';')
            first = False
        else:
            df_files_txt = df_files[df_files['Name'].str.match(f'.*\.{val}')].copy(deep=True)
            df_files_txt.drop('Type', axis=1, inplace=True)
            df_files_txt['Fullpath'] = os.path.join(str(df_files_txt['Path']), str(df_files_txt['Name']))
            df_files_txt["Text"] = df_files_txt['Fullpath'].apply(lambda x: file_to_text(x))
            csv_path = os.path.join(f'{data_folder}', f'{project_name}_text_corpus.csv')
            df_files_txt.to_csv(csv_path, encoding='utf8', sep=';', mode='a', header=False)
        print(df_files_txt)


if __name__ == '__main__':
    load_texts_into_corp()

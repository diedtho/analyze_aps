from pprint import pprint
import pandas as pd

from os_scandir_method import scan_directory

if __name__ == '__main__':
    path_string = "C:\\Users\\diede\\AppData\\Roaming\\Insomnia"
    result_dict = scan_directory(path_string)
    pprint(result_dict)

    df = pd.Series(result_dict).rename_axis('Path').reset_index(name='Entry_List')
    df.to_csv('pre_entries.csv', encoding='utf8', sep=';')
    df_exploded = df.explode('Entry_List', ignore_index=True)
    df_exploded.to_csv('exploded_pre_entries.csv', encoding='utf8', sep=';')
    df_split = pd.DataFrame(df_exploded['Entry_List'].to_list(), columns=['Name', 'Type'])
    df_split.to_csv('splitted_pre_entries.csv', encoding='utf8', sep=';')
    df_entries = pd.concat([df_exploded, df_split], axis=1)
    df_entries.drop('Entry_List', axis=1, inplace=True)
    df_entries.to_csv('entries.csv', encoding='utf8', sep=';')

    print(df.head(25))

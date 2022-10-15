import os
from pathlib import Path
from pprint import pprint

import pandas as pd


def scan_directory_to_results_dict(path_string):
    path = Path(path_string)
    scan_result = [[path.name, 'root']]
    scan_result_dict = {}
    for entry in os.scandir(path):
        if entry.is_dir():
            try:
                scan_result_dict_tmp = scan_directory_to_results_dict(entry)
                scan_result_dict.update(scan_result_dict_tmp)
            except:
                pass
        else:
            scan_result.append([entry.name, 'file'])
    scan_result_dict[str(path)] = scan_result
    return scan_result_dict

def scan_results_dict_to_df(scan_results_dict):
    df = pd.Series(scan_results_dict).rename_axis('Path').reset_index(name='Entry_List')
    #df.to_csv('pre_entries.csv', encoding='utf8', sep=';')
    df_exploded = df.explode('Entry_List', ignore_index=True)
    #df_exploded.to_csv('exploded_pre_entries.csv', encoding='utf8', sep=';')
    df_split = pd.DataFrame(df_exploded['Entry_List'].to_list(), columns=['Name', 'Type'])
    #df_split.to_csv('splitted_pre_entries.csv', encoding='utf8', sep=';')
    df_entries = pd.concat([df_exploded, df_split], axis=1)
    df_entries.drop('Entry_List', axis=1, inplace=True)
    #df_entries.to_csv('entries.csv', encoding='utf8', sep=';')
    return df_entries

def scan_directory_to_results_df(path_string):
    scan_results_dict = scan_directory_to_results_dict(path_string)
    scan_results_df = scan_results_dict_to_df(scan_results_dict)
    return scan_results_df


if __name__ == "__main__":
    path_string = "C:\\Users\\diede\\Documents"
    df_results = scan_directory_to_results_df(path_string)
    pprint(df_results)





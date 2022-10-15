from pprint import pprint
import pandas as pd

from os_scandir_method import scan_directory_to_results_df

if __name__ == '__main__':
    path_string = "C:\\Users\\diede\\AppData\\Roaming\\Insomnia"
    results_df = scan_directory_to_results_df(path_string)
    pprint(results_df)
    results_df.to_csv('results_df.csv', encoding='utf8', sep=';')


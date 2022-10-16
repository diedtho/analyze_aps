from methods.folder_content_to_dataset import dir_df_to_dataset_csv
from methods.os_scandir_method import scan_directory_to_results_df


def get_dir_info_df(path_string, project_name='startfolder', data_folder='../data'):
    results_df = scan_directory_to_results_df(path_string)
    csv_path = f'{data_folder}/{project_name}_content.csv'
    results_df.to_csv(csv_path, encoding='utf8', sep=';')
    dir_df_dict = dir_df_to_dataset_csv(csv_path)
    [df_dir, rootfolder_path] = [dir_df_dict['dataset_df'], dir_df_dict['rootfolder_pathstring']]
    print(df_dir)
    print(rootfolder_path)
    csv_path = f'{data_folder}/{project_name}_dir_df.csv'
    df_dir.to_csv(csv_path, encoding='utf8', sep=';')
    return df_dir

if __name__ == '__main__':
    path_string = "C:\\Users\\diede\\AppData\\Roaming\\Insomnia"
    get_dir_info_df(path_string)

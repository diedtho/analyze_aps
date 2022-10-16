from pathlib import Path
import pandas as pd

def pathstring_to_folderlist(pathstring, rootfolder_pathstring=None):
    folderlist = pathstring.split('\\')
    print(f'folderlist: {folderlist}')
    if rootfolder_pathstring is None:
        print('rootfolder_pathstring is None')
        return None
    else:
        print(f'rootfolder_pathstring is {rootfolder_pathstring}')
        rootfolder_list = rootfolder_pathstring.split('\\')
        rootfolder = rootfolder_list[-1]
        print(f'rootfolder: {rootfolder}')
        if rootfolder in folderlist:
            folderlist_split_length = len(rootfolder_list) - 1
            print(f'folderlist split-length: {folderlist_split_length}')
            folderlist = folderlist[folderlist_split_length:]
            print(f'folderlist cutted: {folderlist}')
            return folderlist

def dir_df_to_dataset_csv(path_string):
    path = Path(path_string)
    df_dir = pd.read_csv(path, encoding='utf8', sep=';', index_col=0)
    #df_dir.to_csv('dir_df.csv', encoding='utf8', sep=';')
    rootfolder_df = df_dir.loc[df_dir['Path'].str.len().sort_values().index].drop_duplicates(subset='Path').reset_index()
    rootfolder_pathstring = rootfolder_df.iloc[0]['Path']
    #rootfolder_df.to_csv('rootfolder_df.csv', encoding='utf8', sep=';')
    df_dir["Path"] = df_dir["Path"]\
        .apply(lambda x: pathstring_to_folderlist(x, rootfolder_pathstring))
    #df_dir.to_csv('df_dir_path_exploded.csv', encoding='utf8', sep=';')
    return {'dataset_df': df_dir, 'rootfolder_pathstring': rootfolder_pathstring}

if __name__ == "__main__":
    path_string = "../data/Insomnia_folder_content.csv"
    dir_df_dict = dir_df_to_dataset_csv(path_string)
    [dir_df, rootfolder_pathstring] = [dir_df_dict['dataset_df'], dir_df_dict['rootfolder_pathstring']]
    dir_df.to_csv('dir_df.csv', encoding='utf8', sep=';')

    print(dir_df)

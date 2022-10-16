from methods.get_directory_information import get_dir_info_df
from methods.load_textfiles_in_corpus import load_texts_into_corp

if __name__ == '__main__':
    path_string = "C:\\Users\\diede\\AppData\\Roaming\\Insomnia"
    project_name = 'Insomnia'
    df = get_dir_info_df(path_string, project_name=project_name, data_folder='data')
    load_texts_into_corp(project_name=project_name, data_folder='data')



from methods.get_directory_information import get_dir_info_df
from methods.load_textfiles_in_corpus import load_texts_into_corp

if __name__ == '__main__':
    # path_string = "I:\\CPROG\\VAP\\DOC\\Spezifikation\\2022"  # ComDev
    path_string = "/home/zarko/AAA_Projektarbeit/"  # home
    # project_name = 'Spezifikationen_2022'  # ComDev
    project_name = 'AAA_Projektarbeit_2'  # home
    df = get_dir_info_df(path_string, project_name=project_name, data_folder='data')
    load_texts_into_corp(project_name=project_name, data_folder='data')



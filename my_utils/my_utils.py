import os
from pathlib import Path


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

def scan_directory_to_results_list_folders(path_string):
    path = Path(path_string)
    scan_result_list = [path.name]
    for entry in os.scandir(path):
        if entry.is_dir():
            try:
                scan_result_list_tmp = scan_directory_to_results_list_folders(entry)
                scan_result_list = scan_result_list + scan_result_list_tmp
            except:
                pass
    return scan_result_list

class RootFolder:

    def __init__(self, path_string):
        self.root_path = Path(path_string)
        self.content_dict = {}
        self.folders_list = []

    def get_subfolder(self):
        self.folders_list = scan_directory_to_results_list_folders(self.root_path)
        return self.folders_list

    def get_content_subfolder_by_name(self, subfolder_name):
        return scan_directory_to_results_dict(self.root_path)

    def get_content(self):
        self.content_dict = scan_directory_to_results_dict(self.root_path)
        return self.content_dict

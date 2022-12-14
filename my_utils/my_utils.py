import os
from pathlib import Path

def index_directories_files(dir_list):
    index_dict = {}
    for dirpath in dir_list:
        temp_index_dict = index_directory_files(dirpath)
        for fname, fpath in temp_index_dict.items():
            if fname not in index_dict.keys():
                index_dict[fname] = [fpath]
            else:
                old_list = index_dict[fname].copy()
                old_list.append(fpath)
                index_dict[fname] = old_list
    return index_dict

def index_directory_files(path_string):
    path = Path(path_string)
    index_result_dict = {}
    for entry in os.scandir(path):
        if entry.is_file():
            index_result_dict[entry.name] = str(entry.path)
    return index_result_dict

def index_directory_subfolders(path_string):
    path = Path(path_string)
    index_result_dict = {}
    index_result_dict[path.name] = [str(path.absolute())]
    for entry in os.scandir(path):
        if entry.is_dir():
            try:
                index_result_dict_tmp = index_directory_subfolders(entry)
                for key, val in index_result_dict_tmp.items():
                    list_new_tmp = val.copy()
                    if key in index_result_dict.keys():
                        list_old_tmp = index_result_dict[key].copy()
                        index_result_dict[key] = [*list_old_tmp, *list_new_tmp]
                    else:
                        index_result_dict[key] = [*list_new_tmp]
            except:
                pass
    return index_result_dict

def scan_directory_subfolders(path_string):
    path = Path(path_string)
    scan_result_dict = {}
    scan_result_dict[str(path.absolute())] = [path.name, path.parts]
    for entry in os.scandir(path):
        if entry.is_dir():
            try:
                scan_result_dict_tmp = scan_directory_subfolders(entry)
                scan_result_dict.update(scan_result_dict_tmp)
            except:
                pass
    return scan_result_dict

class RootFolder:

    def __init__(self, path_string):
        self.root_path = Path(path_string)
        self.folderpathes_dict = {}
        self.folderindices_dict = {}
        self.fileindices_dict = {}

    def get_subfolders(self):
        if len(self.folderpathes_dict) == 0:
            self.folderpathes_dict = scan_directory_subfolders(self.root_path)
        return self.folderpathes_dict

    def get_folderindices(self):
        if len(self.folderindices_dict) == 0:
            self.folderindices_dict = index_directory_subfolders(self.root_path)
        return self.folderindices_dict

    def get_fileindices(self):
        if len(self.folderpathes_dict) == 0:
            self.folderpathes_dict = scan_directory_subfolders(self.root_path)
        if len(self.fileindices_dict) == 0:
            folderpathes_list = list(self.folderpathes_dict.keys())
            self.fileindices_dict = index_directories_files(folderpathes_list)
        return self.fileindices_dict
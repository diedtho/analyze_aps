import os
from pathlib import Path
from pprint import pprint


def scan_directory(path_string):
    path = Path(path_string)
    scan_result = [[path.name, 'root']]
    scan_result_dict = {}
    for entry in os.scandir(path):
        if entry.is_dir():
            try:
                scan_result_dict_tmp = scan_directory(entry)
                scan_result_dict.update(scan_result_dict_tmp)
            except:
                pass
        else:
            scan_result.append([entry.name, 'file'])
    scan_result_dict[str(path)] = scan_result
    return scan_result_dict

if __name__ == "__main__":
    path_string = "C:\\Users\\diede\\Documents"
    result = scan_directory(path_string)
    pprint(result)





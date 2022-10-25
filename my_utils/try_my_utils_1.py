from pprint import pprint
from my_utils import RootFolder

# pathstring = 'K:\CProg\Anlieferungen\EVA'  # ComDev
pathstring = '/home/zarko/AAA_Projektarbeit/'  # home linux

rootdir = RootFolder(pathstring)
subfolders = rootdir.get_subfolders()
print(subfolders)
print('=' * 111)
subfolder_indices = rootdir.get_folderindices()
for index, list in subfolder_indices.items():
    print(index, list)
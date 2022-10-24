from pprint import pprint

from my_utils import RootFolder

pathstring = 'K:\CProg\Anlieferungen\EVA'

rootdir = RootFolder(pathstring)
subfolders = rootdir.get_subfolder()
print(subfolders)

#content_root = rootdir.get_content()
#pprint(content_root)
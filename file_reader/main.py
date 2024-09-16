import shutil
import tempfile
import os
from time import gmtime, strftime
#===========================================

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

custom_prefix = "out" + time
source_folder_path = "/projectnb/msspbc/jordanstout/home/file_reader/files/"
specific_local_directory = "/projectnb/msspbc/jordanstout/home/file_reader/out"
with tempfile.TemporaryDirectory() as temp_dir:
	temp_folder_path = os.path.join(temp_dir, custom_prefix)

	shutil.copytree(source_folder_path, temp_folder_path)
    
	final_path = os.path.join(specific_local_directory, custom_prefix)

	shutil.move(temp_folder_path, final_path)
    
	print(f'Temporary directory with contents moved to: {final_path}')

	for root, dirs, files in os.walk(final_path):
		for name in dirs:
			print(f'Directory: {os.path.join(root, name)}')
		for name in files:
			print(f'File: {os.path.join(root, name)}')








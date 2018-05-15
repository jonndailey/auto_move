import os
import shutil

def main():
	for filename in os.listdir('''directory'''):
		if filename:
			newname = os.path.splitext(filename)[0] 
			new_directory = os.mkdir(newname) 
			shutil.copy(filename,new_directory) 
main()
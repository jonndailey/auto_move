import os
import shutil

def main():
	for filename in os.listdir("/home/jonny/Desktop/testing"):
		if filename:
			newname = os.path.splitext(filename)[0]
			new_directory = os.mkdir(newname) #make directory 
			shutil.copy(filename,new_directory)
main()
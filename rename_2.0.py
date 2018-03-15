# rename_2.0.py
import os


def pdf_rename(files):
	for f_name in files:
		# Check if file is in pdf format
		if '.pdf' not in f_name:
			continue
		else:
			sf_name = f_name.split(' - ')
			if len(sf_name) < 2:
				continue
			else:
				p = sf_name[1]
				os.rename(f_name, p[:-4] +' _ '+ sf_name[0] +'.pdf')

# set working directory
f_names = os.listdir(r'C:\Users\bunyaminu\Desktop\Books')
# check working directory
os.chdir(r'C:\Users\bunyaminu\Desktop\Books')
try:
	for f_name in f_names:
		path = os.path.join(r'C:\Users\bunyaminu\Desktop\Books', f_name)
		fff_names = os.listdir(path)
		os.chdir(path)
		pdf_rename(fff_names)
except WindowsError:
	if True:
		continue
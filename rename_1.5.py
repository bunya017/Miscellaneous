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
				pp = p.replace('.pdf', '')
				try:
					os.rename(f_name, pp +' _ '+ sf_name[0] +'.pdf')
				except WindowsError:
					os.rename(f_name, pp +' _ '+ sf_name[0] +'(1).pdf')


f_names = os.listdir(r'C:\Users\bunyaminu\Desktop\Books\Physics')
os.chdir(r'C:\Users\bunyaminu\Desktop\Books\Physics')
pdf_rename(f_names)

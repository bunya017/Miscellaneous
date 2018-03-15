import os
#import shutil

f_names = os.listdir(r'C:\Users\bunyaminu\Downloads\Video')
os.chdir(r'C:\Users\bunyaminu\Downloads\Video')
for f_name in f_names:
	os.rename(f_name, f_name.replace('Genyoutube.net ', ''))
#	path1 = r'C:\Users\bunyaminu\Downloads\rename\React Js'
#	path2 = r'C:\Users\bunyaminu\Downloads\rename\Machine Learning'
#	path3 = r'C:\Users\bunyaminu\Downloads\rename\Deep Learning'
#	if 'learning reactjs' in f_name.lower():
#		shutil.move(f_name, path1)
#	elif 'data science' in f_name.lower():
#		shutil.move(f_name, path1)
#	elif 'deep learning' in f_name.lower():
#		shutil.move(f_name, path3)

#print('Operation Successful')



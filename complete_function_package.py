#Run this to complete the function package
#It will produce a .zip in the output directory named 'function_package.zip' that can be uploaded to Amazon's Lambda Management Console

import os, pip, shutil

#Determine relevant paths
root_path = os.path.dirname(os.path.realpath(__file__))
function_package_files_path = root_path + '\\function_package_files'
working_path = root_path + '\\working'
output_path = root_path + '\\output'

#Create working directory
if not os.path.exists(working_path):
	print('Making /working/ directory ...')
	os.makedirs(working_path)
	print('SUCCESS!')

#Copy function package files to the working directory
print('Copying files ...')
shutil.copyfile(function_package_files_path + '\\coincheck_data.py', working_path + '\\coincheck_data.py')
shutil.copyfile(function_package_files_path + '\\coincheck_endpoint.py', working_path + '\\coincheck_endpoint.py')
print('SUCCESS!')

#Install dependencies to the working directory
print('Installing dependencies ...')
pip.main(['install', 'requests', '-t', working_path])
print('SUCCESS!')

#Create output directory
if not os.path.exists(output_path):
	print('Making /output/ directory ...')
	os.makedirs(output_path)
	print('SUCCESS!')

#Create zipped function package
print('Zipping archive ...')
shutil.make_archive(output_path + '\\function_package', 'zip', working_path)
print('SUCCESS!')

#Cleanup
print('Cleaning up ...')
shutil.rmtree(working_path)
print('SUCCESS!')

print('Done.')
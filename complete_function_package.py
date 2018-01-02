#Run this to complete the function package
#It will produce a .zip in this directory named 'function_package.zip' that can be uploaded to Amazon's Lambda Management Console

import os, pip, shutil

#Determine relevant paths
root_path = os.path.dirname(os.path.realpath(__file__))
function_package_files_path = root_path + '\\function_package_files'
working_path = root_path + '\\function_package_factory'

#Create working directory
if not os.path.exists(working_path):
	os.makedirs(working_path)

#Copy function package files to the working directory
shutil.copyfile(function_package_files_path + '\\coincheck_data.py', working_path + '\\coincheck_data.py')
shutil.copyfile(function_package_files_path + '\\coincheck_endpoint.py', working_path + '\\coincheck_endpoint.py')

#Install dependencies to the working directory
pip.main(['install', 'requests', '-t', working_path])

#Create zipped function package
shutil.make_archive(root_path + '\\function_package', 'zip', working_path)

#Cleanup
shutil.rmtree(working_path)
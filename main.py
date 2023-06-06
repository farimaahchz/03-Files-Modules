__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
os.chdir('/Users/farimaahchz/Winc/files')
# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

#clean_cache

def clean_cache():
    cache_dir = os.path.join(os.getcwd(), 'cache')
  #check if cache already exists then delete everything in the cache folder
    if os.path.exists(cache_dir):
        for file_name in os.listdir(cache_dir):
            file_path = os.path.join(cache_dir, file_name)
            os.remove(file_path)
    else:
        os.mkdir(cache_dir)

clean_cache()

#cache_zip
import zipfile
def cache_zip(zip_file_path, cache_dir):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir)

cache_zip('/Users/farimaahchz/Winc/files/data.zip', 'cache')

#cached_files
def cached_files():
    cache_dir = os.path.join(os.getcwd(), 'cache')
    abs_file_paths = [os.path.abspath(os.path.join(cache_dir, file_name)) for file_name in os.listdir(cache_dir)]
    return [file_path for file_path in abs_file_paths if os.path.isfile(file_path)]

list_of_files = cached_files()
for file_path in list_of_files:
    print(file_path)

#find_password

import re

def find_password(file_paths):
    password = None
    for file_path in file_paths:
        with open(file_path, 'r') as list_of_files:
            contents = list_of_files.read()
            match = re.search(r'password:\s*(\S+)', contents)
            if match:
                password = match.group(1)
                break
    return password


password = find_password(list_of_files)
print(password)







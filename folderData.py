import os
from readExcel import final_data
import helper
config = helper.read_path_config()
names_object = config['Paths']['folder_path']
file_names = os.listdir(names_object)
choices = ['.JPG', '.jpg']
pdf_files = [i for i in file_names if i.endswith(".pdf")]
jpg_files = [i for i in file_names if i.endswith(tuple(choices))]
text_files = [i for i in file_names if i.endswith(".txt")]
matched_pdf_files = []
matched_jpg_files = []
comp_keys = list(final_data.keys())
for i in comp_keys:
    if i in pdf_files:
        matched_pdf_files.append(i)
    if i in jpg_files:
        matched_jpg_files.append(i)
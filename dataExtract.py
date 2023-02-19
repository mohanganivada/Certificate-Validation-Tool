from folderData import matched_pdf_files, matched_jpg_files
import PyPDF2
import re
from tqdm import tqdm
import pytesseract
import cv2
import helper
import os
import datefinder
from readExcel import names
from mappings import mappings, cname_mappings
config = helper.read_path_config()
names_object = config['Paths']['folder_path']
os.chdir(names_object)
file_names = os.listdir(names_object)
unique_name_pdf = {}
unique_name_jpg = {}
dates = {}
cname_certi = {}
all_data = {}
new_dates = {}
date_pattern1 = "(\d{1,2}(?: |-|/)?(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|June?|July?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?|\d{2})(?:\s|-|/)?\d{4})"
date_pattern2 = "(?:(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May?|June?|July?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{2},\s+\d{4})"
cname1 = '(?<=achieved the certification ,)(.*)(?=,Date of)'
cname2 = '(?<=recognized as a )(.*)(?=. ,Date)'
cname3 = '(?<=verifycerts ,)(.*)(?=er ,)'
cname4 = '(?<=,)(.*)(?=er ,)'
cname5 = '(?<=verifycerts ,)(.*)(?=I ,[A-Z][a-z]*)'
pattern1 = '(\d{3}-\d{4})'
pattern2 = '(\d{3} \d{4})'
pattern3 = '(\d{5,8})'
print("Reading the PDF files.\n")
enc = []
for pdfs in tqdm(matched_pdf_files):
    cert = open(f"{names_object}/{pdfs}", 'rb')
    pdf = PyPDF2.PdfFileReader(cert, strict=False)
    if pdf.is_encrypted:
        enc.append(pdfs)
    else:
        Obj = pdf.getPage(0)
        text = (Obj.extractText())
        text = text.replace('\n', ' ,')
        text = text.replace('\xa0', ' ').replace(
            '\n', " ").replace('�', 'fi')
        for pattern in names:
            if re.search(pattern, text, re.IGNORECASE):
                unique_name_pdf[pdfs] = {
                    'Name': pattern
                }
                break
        date_found = re.search(
            "|".join([date_pattern2, date_pattern1]), text)
        if date_found == None:
            dates[pdfs] = {
                'Date': "Error"
            }
        else:
            dates[pdfs] = {
                'Date': date_found.group(0)
            }
        certification_name = re.search(
            "|".join([cname1, cname2,cname3,cname4,cname5]), text, re.IGNORECASE)
        if certification_name == None:
            cname_certi[pdfs] = {
                'Certification Name': "Could Not Extract Certification Name from File.",
                'Actual Certification Name': 'Could Not Extract Certification Name from File.'
            }
        else:
            certification_name = certification_name.group(0)
            certification_name = str(certification_name).replace(
                'Micr osoft Cer tified: Azur e', 'Microsoft Certified: Azure').replace('Administrat or Associat e','Administrator Associate')
            certification_name = str(certification_name).replace(
                'Micr osoft Cer tified: Azur e Administrat or Associat e', 'Microsoft Certified: Azure Administrator Associate')
            cname_certi[pdfs] = {
                'Certification Name': certification_name,
                'Actual Certification Name' : 'Could Not Extract Certification Name from File.'
            }
        for i in cname_mappings:
            if str(certification_name).lower().removesuffix(" ") == str(mappings[i]['Value']).lower().removesuffix(" "):
                cname_certi[pdfs] = {
                    'Certification Name': i,
                    'Actual Certification Name': str(mappings[i]['Value']).lower().removesuffix(" ")
                }
keys_pdf = list(unique_name_pdf.keys())
for i in keys_pdf:
    if dates[i]['Date'] == "Error" or re.search("|".join([pattern1, pattern2, pattern3]), dates[i]['Date']):
        new_dates[i] = {
            'Date': "Error"
        }
    else:
        matches = datefinder.find_dates(dates[i]['Date'])
        for k in matches:
            new_dates[i] = {
                'Date': str(k).split(' ')[0]
            }
    all_data[i] = {
        'Name': unique_name_pdf[i]['Name'],
        'Exam Pass Date': new_dates[i]['Date'],
        'Certification Name': cname_certi[i]['Certification Name'],
        'Actual Certification Name' : cname_certi[i]['Actual Certification Name']
        }
print('\n')
print("Reading the JPG files.")
print('\n')
for images in tqdm(matched_jpg_files):
    img = cv2.imread(images)
    data = pytesseract.image_to_string(img)
    for pattern in names:
        if re.search(pattern, data, re.IGNORECASE):
            unique_name_jpg[images] = {
                'Name': pattern
            }
    date_found = re.search(
        "|".join([date_pattern2, date_pattern1]), data)
    if date_found == None:
        dates[images] = {
            'Date': "Error"
        }
    else:
        dates[images] = {
            'Date': date_found.group(0)
        }
    certification_name = re.search(
        "|".join([cname1, cname2,cname3,cname4,cname5]), data, re.IGNORECASE)
    if certification_name == None:
        cname_certi[images] = {
            'Certification Name': "Could Not Extract Certification Name from File.",
            'Actual Certification Name' : 'Could Not Extract Certification Name from File.'
        }
    else:
        certification_name = certification_name.group(0)
        certification_name = str(certification_name).replace(
            'Micr osoft Cer tified: Azur e', 'Microsoft Certified: Azure')
        certification_name = str(certification_name).replace(
                'Micr osoft Cer tified: Azur e Administrat or Associat e', 'Microsoft Certified: Azure Administrator Associate')
        cname_certi[images] = {
            'Certification Name': certification_name,
            'Actual Certification Name' : 'Could Not Extract Certification Name from File.'
        }
    for i in cname_mappings:
        if str(certification_name).lower().removesuffix(" ") == str(mappings[i]['Value']).lower().removesuffix(" "):
            cname_certi[images] = {
                'Certification Name': i,
            'Actual Certification Name' : str(mappings[i]['Value']).lower().removesuffix(" ")
        }
print("Done.")
print("\n")
keys_jpg = list(unique_name_jpg.keys())
for i in keys_jpg:
    if dates[i]['Date'] == "Error" or re.search("|".join([pattern1, pattern2, pattern3]), dates[i]['Date']):
        new_dates[i] = {
            'Date': "Error"
        }
    else:
        matches = datefinder.find_dates(dates[i]['Date'])
        for k in matches:
            new_dates[i] = {
                'Date': str(k).split(' ')[0]
            }
    all_data[i] = {
        'Name': unique_name_jpg[i]['Name'],
        'Exam Pass Date': new_dates[i]['Date'],
        'Certification Name': cname_certi[i]['Certification Name'],
        'Actual Certification Name' : cname_certi[i]['Actual Certification Name']
    }
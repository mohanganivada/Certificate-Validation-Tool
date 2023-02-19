from readExcel import final_data
from folderData import matched_pdf_files
import PyPDF2
import re
import helper
from readExcel import names
from readExcel import certification_name
from readExcel import pass_date
config = helper.read_config()

az_certification = []
for i in range(len(matched_pdf_files)):
    if final_data[matched_pdf_files[i]]['Certification Name'] == "Salesforce Certified Administrator":
    #if final_data[matched_pdf_files[i]]['Certification Name'] == "Databricks Accredited Lakehouse Fundamentals":
        az_certification.append(matched_pdf_files[i])
    #print(az_certification)
rst=names
dates = []
matched_name = []
cname = {}
for i in range(len(az_certification)):
    cert = open(
        f"{config['Paths']['folder_path']}\\{az_certification[i]}", 'rb')
    try:
        pdf = PyPDF2.PdfFileReader(cert, strict=False)
        Obj = pdf.getPage(0)
        text = (Obj.extractText())
        text = text.replace('\n',' ,')
        print(text)
    except:
        print('\n')
    # print('----------------------------')
    
    cname1 = '(?<=verifycerts ,)(.*)(?=or ,)'
    #cname1 = '(?<=of ,)(.*)(?= ,is)'
    certification_name = re.search("|".join([cname1]), text)  

    if certification_name == None:

        cname[az_certification[i]] = {

                'Certification Name': "Error"

            }

    else:

        cname[az_certification[i]] = {

                'Certification Name': (certification_name.group(0))

               

            }

     

print(cname)
        
#print(cname)
    #print('--------------------------------------------------------------------------------')



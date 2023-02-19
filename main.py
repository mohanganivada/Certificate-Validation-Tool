from readExcel import certificate_name
from folderData import pdf_files, text_files, jpg_files, matched_pdf_files, matched_jpg_files
from resultExcel import my_wb , final_result , new
import helper
from datetime import datetime
config = helper.read_path_config()
result_path = config['Paths']['result_path']
print(f"Total no of Matched pdf Files : {len(matched_pdf_files)}")
print(f"Total no of Matched jpg Files : {len(matched_jpg_files)}")
print(f"Total Number of Accepted Certificates : {len([i for i in new if final_result[i]['Status'] == 'Accepted.'])} ")
print(f"Total Number of Rejected Certificates : {len([i for i in new if final_result[i]['Status'] == 'Rejected.'])} ")
print(f"Reason of rejection : Employee Name not Matched : {len([i for i in new if final_result[i]['Reason'] == 'Employee Name not Matched'])}")
print(f"Reason of rejection : Certification Name not Matched : {len([i for i in new if final_result[i]['Reason'] == 'Certification Name not Matched'])}")
print(f"Reason of rejection : Exam Pass Date not Matched : {len([i for i in new if final_result[i]['Reason'] == 'Exam Pass Date not Matched'])}")
print(f"Files not in .pdf, .jpg or .txt format in temp folder : {len(certificate_name)-(len(pdf_files)+len(jpg_files)+len(text_files))}")
dt_string = datetime.now().strftime("%d-%m-%Y")
result = f'{result_path}/Results_AZ900_{dt_string}'
my_wb.save(f"{result}.xlsx")
print(f"Results stored in Excel as '{result}'")
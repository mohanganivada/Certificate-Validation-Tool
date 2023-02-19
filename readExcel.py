import pandas as pd
import helper
from mappings import cname_mappings
config = helper.read_path_config()
mapping = helper.read_certificate_mapping_config()
excel_path = config['Paths']['excel_path']
df = pd.read_excel(excel_path)
names = df['EmployeeName'].to_list()
certification_name = df['CertificationName'].to_list()
pass_date = df['ExamPassDate'].to_list()
certificate_name = df['ActualCertificationName'].to_list()
status = df['Status'].to_list()
empcode = df['EmployeeCode'].to_list()
final_data = {}

for i in range(len(names)):
    if status[i] == 'Applied':
        if str(certification_name[i]).lower() in cname_mappings:
            final_data[certificate_name[i]] = {
                'Certification Name': certification_name[i],
                'Employee Code': empcode[i],
                'Exam Pass Date': str(pass_date[i]).split(" ")[0],
                'Name': names[i],
            }
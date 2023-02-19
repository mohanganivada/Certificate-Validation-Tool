from dataExtract import all_data, keys_pdf, keys_jpg
from readExcel import final_data
from folderData import matched_pdf_files, matched_jpg_files
final_result = {}
for i in matched_pdf_files:
    if i in keys_pdf:
        final_result[i] = {
            'Certification Name': all_data[i]['Certification Name'],
            'Actual Certificate Name' : all_data[i]['Actual Certification Name'],
            'Exam Pass Date': all_data[i]['Exam Pass Date'],
            'Name': all_data[i]['Name'],
            'Status': '',
            'Reason': ''
        }
    else:
        final_result[i] = {
            'Certification Name': final_data[i]['Certification Name'],
            'Actual Certificate Name' : "Could Not Extract Certification Name from File.",
            'Exam Pass Date': final_data[i]['Exam Pass Date'],
            'Name': final_data[i]['Name'],
            'Status': '',
            'Reason': ''
        }
for items in matched_pdf_files:
    if items in keys_pdf:
        if final_data[items]['Exam Pass Date'] == all_data[items]['Exam Pass Date']:
            final_result[items]['Status'] = "Exam Pass Date is Matched"
            final_result[items]['Reason'] = "Ongoing for Certification Validation"
            if final_result[items]['Certification Name'] == str(final_data[items]['Certification Name']).lower():
                final_result[items]['Status'] = "Accepted."
                final_result[items]['Reason'] = "Approve the Request."
            else:
                final_result[items]['Status'] = "Rejected."
                final_result[items]['Reason'] = "Certification Name not Matched"
        else:
            final_result[items]['Status'] = "Rejected."
            final_result[items]['Reason'] = "Exam Pass Date not Matched"
    else:
        final_result[items]['Status'] = "Rejected."
        final_result[items]['Reason'] = "Employee Name not Matched"

for i in matched_jpg_files:
    if i in keys_jpg:
        final_result[i] = {
            'Certification Name': all_data[i]['Certification Name'],
            'Actual Certificate Name' : all_data[i]['Actual Certification Name'],
            'Exam Pass Date': all_data[i]['Exam Pass Date'],
            'Name': all_data[i]['Name'],
            'Status': '',
            'Reason': ''
        }
    else:
        final_result[i] = {
            'Certification Name': final_data[i]['Certification Name'],
            'Actual Certificate Name' : "Could Not Extract Certification Name from File.",
            'Exam Pass Date': final_data[i]['Exam Pass Date'],
            'Name': final_data[i]['Name'],
            'Status': '',
            'Reason': ''
        }
for items in matched_jpg_files:
    if items in keys_jpg:
        if final_data[items]['Exam Pass Date'] == all_data[items]['Exam Pass Date']:
            final_result[items]['Status'] = "Exam Pass Date is Matched"
            final_result[items]['Reason'] = "Ongoing for Certification Validation"
            if str(final_result[items]['Certification Name']).lower() == str(final_data[items]['Certification Name']).lower():
                final_result[items]['Status'] = "Accepted."
                final_result[items]['Reason'] = "Approve the Request."
            else:
                final_result[items]['Status'] = "Rejected."
                final_result[items]['Reason'] = "Certification Name not Matched"
        else:
            final_result[items]['Status'] = "Rejected."
            final_result[items]['Reason'] = "Exam Pass Date not Matched"
    else:
        final_result[items]['Status'] = "Rejected."
        final_result[items]['Reason'] = "Employee Name not Matched"
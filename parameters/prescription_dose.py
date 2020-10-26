'''
this file are used to deal with prescription_dose parameter in DICOM,
currently, including
extract_prescription_dose,
validate_prescription_dose
'''


import pydicom

"""
Method1 : extract_prescription_dose
extract all prescription_dose from file_path
if you want use this function,
please upload one file_path which is a dicom_file file
"""


def extract_prescription_dose(file_path):
    # step1: read one dicom_file file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []

    # step2. find all prescription dose from ds
    try:
        for drs in ds.DoseReferenceSequence:
            if hasattr(drs, 'TargetPrescriptionDose'):
                res.append(drs.TargetPrescriptionDose)
    except AttributeError as err:
        print(("OS error: {0} in "+file_path).format(err))

    # step3: Use 'set' to remove the same value
    res = list(set(res))
    return res

'''
Method2 : validate_prescription_dose
validate prescription_dose with truth value;
truthcase: the standard value for given case;
extracted_value: the prescription_dose extracted from given DICOM file.
'''


def validate_prescription_dose(truthcase, extracted_value, writer, case_number):
    # print(("wedge:"))
    # print("     truth case in truth table is", end=": ")
    writer.writerow(("********prescription_dose********", ""))
    truth_prescription_dose = truthcase['prescription dose']
    # print(truth_wedge)
    writer.writerow(("truth case in case "+str(case_number), str(truth_prescription_dose)+","))
    # print("     extracted value is", end=": ")
    # print(extracted_value)
    writer.writerow(("extracted value: ", extracted_value))
    if extracted_value==str(int(truth_prescription_dose)):
        return True
    else:
        return False

'''
truth case:
2
50/25
900/3 MU
45/3
24/2
48/4
3
20
'''

'''
extracted value:
YellowLvlIII_1a.dcm: 1a ["2.0"]
2a: ["2.0"]
3a: ["2.0"]
4a: ["2.0"]`
6a: ["50.0"]
8b: ["50.0"]
需要一份dicom structure.
'''

file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LIII DICOM samples/YellowLvlIII_8b.dcm"
res = extract_prescription_dose(file_path)
# print("-------------------------")
# print(res)

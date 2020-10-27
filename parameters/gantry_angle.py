'''
this file are used to deal with gantry angle parameter in DICOM,
currently, including
extract_gantry_angle,
validate_gantry
'''

import pydicom

"""
Method1 : extract_gantry_angle
extract all gantry angle from file_path
if you want use this function,
please upload one file_path which is a dicom_file file
"""

def extract_gantry_angle(file_path):
    # step1: read one dicom_file file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
        # print(ds)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    # step2: find all gantry angles from ds
    # gantry angle is located in dicomData.BeamSequence.Item_1.ControlPointSequence.Item_1.GantryAngle
    try:
        for bs in ds.BeamSequence:
            for cp in bs.ControlPointSequence:
                if hasattr(cp, 'GantryAngle'):
                    res.append(cp.GantryAngle)
    except AttributeError as err:
        print(("OS error: {0} in "+file_path).format(err))

    # step3: Use 'set' to remove the same value
    res = list(set(res))
    return res




'''
Method2 : validate_gantry
validate gantry angle with truth value;
truthcase: the standard value for given case;
extracted_value: the gantry angle extracted from given DICOM file.
'''

def validate_gantry(truthcase, extracted_value, writer, case_number):

    # step1: show prompt information to csv file
    writer.writerow(("********gantry angle*********", ""))
    # print(("gantry angle:"))
    # print("     truth case in truth table is", end =": ")
    truth_gantries = truthcase['gantry'].split(",")
    truth_gantries = [int(x) for x in truth_gantries]
    truth_gantries.sort()
    # print(truth_gantries)
    writer.writerow(("truth case in case "+str(case_number), truth_gantries))
    extracted_value = [int(x) for x in extracted_value]
    extracted_value.sort()
    # print("     extracted value is", end =": ")
    # print(extracted_value)
    writer.writerow(("extracted value:", extracted_value))

    # step2: validate
    if len(extracted_value) != len(truth_gantries):
        return False
    for i in range(len(truth_gantries)):
        if extracted_value[i] != truth_gantries[i]:
            return False
    return True


import openpyxl
import os
import pydicom

'''
validate collimator
Beam Limiting Device Angle
'''
def extract_collimator(file_path):
    # step1: read one dicom_file file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    # print(ds)
    # step2: extract collimator from ds
    # BeamSequence, Control Point Sequence, BeamLimitingDeviceAngle
    i =0
    try:
        for bs in ds.BeamSequence:
            if hasattr(bs, 'ControlPointSequence'):
                for cps in bs.ControlPointSequence:
                    if hasattr(cps, 'BeamLimitingDeviceAngle'):
                        res.append(cps.BeamLimitingDeviceAngle)
    except AttributeError as err:
        print("OS error: {0}".format(err))

    # step3: Use 'set' to remove the same value
    res = list(set(res))
    return res


'''
Method1 : validate_gantry
validate gantry angle with truth value;
truthcase: the standard value for given case;
datalist: the gantry angle extracted from given DICOM file.
'''

'''
truth case have 4 kinds values including: 0, 90, not 0, -,
extracted case including: (0.0)  (5.0), (270),(355)
firstly base on truth case:
if 0:
    length>0 fail, length==0 and int(0)==0;
if not 0:
    length>0 true, if length==0 and int(0)==0 false; else true
if 90:
    length=1 and int() ==90
-:
    if length==0 and int(0)==0 true.
... ...
'''

def validate_collimator(truthcase, extracted_value, writer,case_number):
    print(("------collimator---------"," "))
    writer.writerow(("********collimator***************", ""))
    print("     truth case in truth table is", end =": ")
    truth_collimator = truthcase['collimator']
    print(truth_collimator)
    writer.writerow(("truth case is in case "+ str(case_number), truth_collimator))
    print("     extracted value is", end=": ")
    print(extracted_value)
    writer.writerow(("extracted value is: ", extracted_value))

    if truth_collimator =="0":
        if len(extracted_value)== 1 and int(extracted_value[0]) == 0:
            return True
        else:
            return False
    elif truth_collimator =="90":
        if len(extracted_value) == 1 and int(extracted_value[0]) == 90:
            return True
        else:
            return False
    elif truth_collimator =="not 0":
        if len(extracted_value) ==0:
            return False
        if len(extracted_value) ==1 and int(extracted_value[0]) != 0:
            return True
        elif len(extracted_value) >1 :
            for value in extracted_value:
                if int(value)!=0:
                    return True
            else:
                return False
    elif truth_collimator =="-":
        return True


'''
truth table: 0， 90, not 0, -

0: len==1 and ==0;
90: len==1 and ==90
not 0: int()==0 return flse;
-: return true?
'''

'''
extracted value which are num array  
YellowLvlIII_7a.dcm: ["0.0"]
YellowLvlIII_7b.dcm: ["0.0", "355.0"]
ACDSLevelII3_2a.dcm: ["0.0"]
ACDSLevelII3_3a.dcm: ["0.0"]
ACDSLevelII3_6a.dcm ["0.0"]
ACDSLevelII3_7a.dcm ["270.0"]
ACDSLevelII3_8a.dcm ["0.0"]
ACDSLevelII3_13a.dcm ["0.0"]
ACDSLevelII3_14a.dcm ["0.0"]
ACDSLevelII3_14b.dcm ["5.0"]
'''


# file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LII DICOM samples/ACDSLevelII3_14b.dcm"
# res = extract_collimator(file_path)
# # truthcase = auto_validate.read_truth_table(6)
# # truth_collimator = truthcase['collimator']
# # print(truth_collimator)
#
# print(res)
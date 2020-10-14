
import openpyxl
import os
import pydicom
import auto_validate

'''
validate collimator
Beam Limiting Device Angle
'''
def extract_collimator(file_path):
    # step1: read one dicom file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    # print(ds)
    # step2: extract collimator from ds
    # BeamSequence, Control Point Sequence, BeamLimitingDeviceAngle
    #
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

def validate_collimator(truthcase, extracted_value):
    print("collimator:")
    print("     truth case in truth table is", end =": ")
    truth_gantries = truthcase['collimator'].split(",")
    truth_gantries = [int(x) for x in truth_gantries]
    truth_gantries.sort()
    print(truth_gantries)
    extracted_value = [int(x) for x in extracted_value]
    extracted_value.sort()
    print("     extracted value is", end =": ")
    print(extracted_value)
    if len(extracted_value) != len(truth_gantries):
        return False
    # print(truth_gantries)
    # print(extracted_value)
    for i in range(len(truth_gantries)):
        if extracted_value[i] != truth_gantries[i]:
            return False
    return True


'''
kinds in real value:  
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

file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LII DICOM samples/ACDSLevelII3_14b.dcm"
res = extract_collimator(file_path)
truthcase = auto_validate.read_truth_table(6)
truth_collimator = truthcase['collimator']
print(truth_collimator)

print(res)
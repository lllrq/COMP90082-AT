'''
this file will be deleted because:
after talking with client,we found that these params cannot be extracted from DICOM file.

'''

import openpyxl
import os
import pydicom


def extract_isocentre(file_path):
    # step1: read one dicom file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    # print(ds)
    # step2. find all gantry angles from ds
    # Isocenter Position
    # Control Point Sequence
    # Beam Sequence
    # print(ds)
    try:
        for bs in ds.BeamSequence:
            if hasattr(bs, 'ControlPointSequence'):
                for cps in bs.ControlPointSequence:
                    if hasattr(cps, 'IsocenterPosition'):
                        res.append(cps.IsocenterPosition)
    except AttributeError as err:
        print("OS error: {0}".format(err))
    return res
    # step3: Use 'set' to remove the same value
    tmp =[]
    for r1 in res:
        r1.sort()
        for t in tmp:
            if r1 ==t:
                break
        else:
            tmp.append(r1)
    return tmp


'''
actual value: 
YellowLvlIII_7a.dcm: [[-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6], [-0.5, -105.1, -7.6]]
1a: [[-0.5, -105.1, -0.1]]
2a: [[-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6]]
3a: [[-0.5, -31.8, -7.6]]
4a: [[-0.5, -31.8, -7.6]]
YellowLvlIII_6a.dcm: [[-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6], [-0.5, -31.8, -7.6]]
6b: [[-0.5, -31.8, -7.6]]
YellowLvlIII_8b.dcm: [[-0.5, -31.8, -7.6]]



'''

file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LIII DICOM samples/YellowLvlIII_8b.dcm"
res = extract_isocentre(file_path)
# print(res)
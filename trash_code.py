'''
This file is convenient for our development.
when we finish this development, we will delete it and don't care about it.
'''

import pydicom


# file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LII DICOM samples/YellowLvlIII_7a.dcm"
# res = extract_gantry_angle(file_path)
# print(res)


# Beam Dose Point SSD--    Referenced Dose Reference Sequence--
# Control Point Sequence --   Beam Sequence


#  2.SSD? why this value is not same format with the truth value
def extract_SSD(file_path):
    # step1: read one dicom file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    print(ds)
    # step2. find all gantry angles from ds
    # gantry angle is located in dicomData.BeamSequence.Item_1.ControlPointSequence.Item_1.GantryAngle
    try:
        for bs in ds.BeamSequence:
            for cp in bs.ControlPointSequence:
                if hasattr(cp, 'ReferencedDoseReferenceSequence'):
                    for rdrs in cp.ReferencedDoseReferenceSequence:
                        if hasattr(rdrs, 'BeamDosePointSSD'):
                            res.append(rdrs.BeamDosePointSSD)
    except AttributeError as err:
        print("OS error: {0}".format(err))

    # step3: Use 'set' to remove the same value
    res = list(set(res))
    return res


file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LII DICOM samples/YellowLvlIII_7a.dcm"
res = extract_SSD(file_path)
print(res)



'''
# 3. wedge
def extract_wedge(file_path):
    # step1: read one dicom file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    # print(ds)
    # step2. find all gantry angles from ds
    # wedge:
    # Number of Wedges
    # Beam Sequence

    try:
        for bs in ds.BeamSequence:
            if hasattr(bs, 'NumberOfWedges'):
                res.append(bs.NumberOfWedges)
    except AttributeError as err:
        print("OS error: {0}".format(err))

    # step3: Use 'set' to remove the same value
    res = list(set(res))
    return res


file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LII DICOM samples/YellowLvlIII_7a.dcm"
res = extract_wedge(file_path)
print(res)
'''


'''
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
    print(ds)
    try:
        for bs in ds.BeamSequence:
            if hasattr(bs, 'ControlPointSequence'):
                for cps in bs.ControlPointSequence:
                    if hasattr(cps, 'IsocenterPosition'):
                        res.append(cps.IsocenterPosition)
    except AttributeError as err:
        print("OS error: {0}".format(err))

    # step3: Use 'set' to remove the same value
    # res = list(set(res))
    return res

file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LII DICOM samples/YellowLvlIII_7a.dcm"
res = extract_isocentre(file_path)
print(res)
'''

'''
def extract_isocentre(file_path):
    # step1: read one dicom file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    print(ds)
    # step2. find all gantry angles from ds
    # Isocenter Position
    # Control Point Sequence
    # Beam Sequence
    print(ds)
    try:
        for bs in ds.BeamSequence:
            if hasattr(bs, 'ControlPointSequence'):
                for cps in bs.ControlPointSequence:
                    if hasattr(cps, 'IsocenterPosition'):
                        res.append(cps.IsocenterPosition)
    except AttributeError as err:
        print("OS error: {0}".format(err))

    # step3: Use 'set' to remove the same value
    # res = list(set(res))
    return res

file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LII DICOM samples/YellowLvlIII_7a.dcm"
res = extract_isocentre(file_path)
print(res)

'''
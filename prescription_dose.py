
import pydicom

def extract_prescription_dose(file_path):
    # step1: read one dicom_file file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    # print(ds)
    # step2. find all prescription dose from ds
    # Number of Wedges
    # Beam Sequence
    # Dose Reference Sequence

    try:
        for drs in ds.DoseReferenceSequence:
            if hasattr(drs, 'TargetPrescriptionDose'):
                res.append(drs.TargetPrescriptionDose)
    except AttributeError as err:
        print("OS error: {0}".format(err))

    # step3: Use 'set' to remove the same value
    res = list(set(res))
    return res

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
4a: ["2.0"]
6a: ["50.0"]
8b: ["50.0"]
需要一份dicom structure.
'''

file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LIII DICOM samples/YellowLvlIII_8b.dcm"
res = extract_prescription_dose(file_path)
print("-------------------------")
print(res)

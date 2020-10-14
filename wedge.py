
import pydicom

# 3. wedge
def extract_wedge(file_path):
    # step1: read one dicom file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    # print(ds)
    # step2. find all wedge from ds
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

def validate_wedge(truthcase, extracted_value):
    print("wedge:")
    print("     truth case in truth table is", end=": ")
    truth_wedge = truthcase['wedge']
    print(truth_wedge)
    print("     extracted value is", end=": ")
    print(extracted_value)

    if truth_wedge == "no wedge":
        # if there only one value, and equal 0, we think that no wedge?
        if len(extracted_value) == 1 and extracted_value[0]== 0:
            return True
        elif len(extracted_value) == 0:
            return True
        else:
            return False
    elif truth_wedge == "0":
        if len(extracted_value) == 1 and extracted_value[0] == 0:
            return True
        else:
            return False
    elif truth_wedge== "30,0,30":
        if len(extracted_value) == 2:
            if truth_wedge[0] == 30 and truth_wedge[1] == 0:
                return True
            elif truth_wedge[1] == 30 and truth_wedge[0] == 0:
                return True
            else:
                return False
        else:
            return False
    elif truth_wedge== "60":
        if len(extracted_value) == 1 and extracted_value[0] == 60:
            return True

'''
some truth case in truth case table:
0
30,0,30
60
no wedge
'''

'''
some extracted case: a1 means that YellowLvlIII_7a.dcm file
YellowLvlIII_7a.dcm: ["0"]
1a: ["0"]
2a: ["0", "1"]
3a: ["0"]
4a: ["1"]
6a: ["0"]
8b: ["0"]
YellowLvlIII_1a_Dose.dcm: [] because no 'FileDataset' object has no attribute 'BeamSequence'
'''

file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LIII DICOM samples/YellowLvlIII_2a.dcm"
res = extract_wedge(file_path)
print(res)
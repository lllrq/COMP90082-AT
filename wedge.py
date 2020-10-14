
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



'''
truth case:
0
30,0,30
60
no wedge
'''

'''
extracted:>
YellowLvlIII_7a.dcm: ["0"]
1a: ["0"]
2a: ["0", "1"]
3a: ["0"]
4a: ["1"]
6a: ["0"]
8b: ["0"] 
YellowLvlIII_1a_Dose.dcm: [] because no 'FileDataset' object has no attribute 'BeamSequence'
'''

file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LIII DICOM samples/YellowLvlIII_1a_Dose.dcm"
res = extract_wedge(file_path)
print(res)


import pydicom
# import auto_validate

def extract_SSD(file_path):
    # step1: read one dicom file from given path and assigns value to the variable ds
    try:
        ds = pydicom.dcmread(file_path, force=True)
    except IOError:
        print("Error: The file was not found or failed to read")
    res = []
    # print(ds)
    # step2. find all gantry angles from ds
    # SSD:
    # Source to Surface Distance
    # Control Point Sequence
    try:
        for bs in ds.BeamSequence:
            cp = bs.ControlPointSequence[0]
            if hasattr(cp, 'SourceToSurfaceDistance'):
                res.append(cp.SourceToSurfaceDistance)
    except AttributeError as err:
        print("OS error: {0}".format(err))

    # step3: Use 'set' to remove the same value
    # res = list(set(res))
    return res

'''
validate SSD with truth value;
truthcase: the standard value for given case;
datalist: the SSD extracted from given DICOM file.
'''

# ["851.9", "894.2", "926.7", "895.7", "851.9", "1000.0"]
# - mean non value？
def validate_SSD(truthcase, extracted_values):
    truth_SSD = truthcase['SSD'].split(",")

    print("SSD:")
    print("     truth case is", end =": ")
    print(truth_SSD)
    #  no extracted value and truth SSD is -
    if (len(extracted_values)==0 and len(truth_SSD)==1 and truth_SSD[0]=='-'):
        return True
    elif len(extracted_values)==0:
        return False
    extracted_values = [int(int(i)/10) for i in extracted_values]

    print("     extracted value is",  end =": ")
    print(extracted_values)

    normalize_extracted_values = []
    if len(extracted_values) == 1:
        if abs((extracted_values[0]) - 100) <= 1.5:
            normalize_extracted_values.append( '100')
        elif abs((extracted_values[0]) - 86) <= 1.5:
            normalize_extracted_values.append('86')
        elif abs((extracted_values[0]) - 93) <= 1.5:
            normalize_extracted_values.append('93')
        elif abs((extracted_values[0]) - 90) <= 1.5:
            normalize_extracted_values.append('90')
    elif len(extracted_values) == 3:
        if abs((extracted_values[0]) - 86) <= 1.5 and abs((extracted_values[1]) - 93) <= 1.5 and abs(
                (extracted_values[2]) - 86) <= 1.5:
            normalize_extracted_values.append('86')
            normalize_extracted_values.append('93')
            normalize_extracted_values.append('86')
        else:
            return False
    elif len(extracted_values) > 5:
        if abs((extracted_values[1]) - 89) <= 1.5 and abs((extracted_values[2]) - 93) <= 1.5 and abs(
                (extracted_values[3]) - 89) <= 1.5:
            normalize_extracted_values.append('?')
            normalize_extracted_values.append('89')
            normalize_extracted_values.append('93')
            normalize_extracted_values.append('89')
            normalize_extracted_values.append('?')
        else:
            return False
    if len(normalize_extracted_values)!=len(truth_SSD):
        return False
    for i in range(len(normalize_extracted_values)):
        if truth_SSD[i] != normalize_extracted_values[i]:
            return False
    return True


# file_path = "/Users/yaozhiyuan/myunimelb/semster3/software project/DICOM/LII DICOM samples/YellowLvlIII_7a.dcm"
#
# truthcase = auto_validate.read_truth_table(6)
# extracted_values = extract_SSD(file_path)
# res = validate_SSD(truthcase, extracted_values)
# print("------ssd------")
# print(res)
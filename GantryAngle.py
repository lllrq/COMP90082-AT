import pydicom
import csv
import os

"""
Method1 : 
extract all gantry angle from file_path  
if you want use this function, 
please upload one file_path which is a dicom file
"""


def extract_gantry_angle(file_path):
    ds = pydicom.dcmread(file_path, force=True)
    list1 = []
    for bs in ds.BeamSequence:
        for cp in bs.ControlPointSequence:
            if hasattr(cp, 'GantryAngle'):
                list1.append(cp.GantryAngle)
    list1 = list(set(list1))
    print(list1)
    return list1


'''
Method2:  
this function toCSVFile is used to 
convert param dataList to one csv file which contain value and result(pass/fail); 
paramType means: which param you want to   
'''


def to_csv_file(dataList, destination, paramType="GantryAngle"):
    csvFile = open(destination, 'w', newline='')
    try:
        writer = csv.writer(csvFile)
        writer.writerow((paramType + " #", 'value', 'result'))
        for i in range(len(dataList)):
            flag = dataList[i] > 50 and dataList[i] < 120
            writer.writerow((i, dataList[i], flag))
    finally:
        csvFile.close()


def TestGantryAngle(file_path):
    ds = pydicom.dcmread(file_path, force=True)
    list1 = [150.0, 60.0]


file_path = "/Users/yaozhiyuan/Desktop/YellowLvlIII_7a.dcm"

'''
Method3:  
this function auto_validate is used to 
auto validate file from DICOM file and output csv file 
'''


def auto_validate(file_path):
    dataList = extract_gantry_angle(file_path)
    destination = file_path[0:file_path.rfind("/")] + "/test1.csv"
    to_csv_file(dataList, destination)
    print("congratulation, validate success!")
    print("the output file is located in " + destination)




filePath = os.path.split(os.path.realpath(__file__))[0] + "/DICOM_File_Path"
file = open(filePath)
for line in file:
    auto_validate(line)
file.close()





"""
at the beginning I try that, ignore them!
"""
'''
file_path = "/Users/seven/Desktop/YellowLvlIII_7a_Dose_RxA_Bm1.dcm"
ds = pydicom.dcmread(file_path,force=True)

SPP = ds.SamplePerPixel
PI = ds.PhotometricInterpretation
Freams = ds.NumberOfFrames
print("Sample per Pixel = " + (str)(SPP))

print("------patientName:-------- ")
print(ds.PatientName)
print("-----all tags:-------- ")

print(ds.dir())
print("-----all tags name including pat ------- ")
print(ds.dir('pat'))


print(ds.data_element('PatientID'))
print(ds.data_element('PatientID').VR, ds.data_element('PatientID').value)

print("----other----")
print(ds.dir('LargestImagePixelValue'))
print(ds.data_element('LargestImagePixelValue'))


#  'PixelData', 'PixelRepresentation', 'PixelSpacing',
print("----other1----")
print(ds.data_element('PixelData'))
pixel_bytes = ds.PixelData
# i=0
# while i<10000:
#    print(pixel_bytes[i])
#    i+=1
# for index,i in pixel_bytes:
#     if(index>100):
#         break
#     print(i)
print("----other2----")
print(ds.data_element('PixelRepresentation'))
print("----other3----")
print(ds.data_element('PixelSpacing'))




pix = ds.pixel_array
print(pix.shape)

pylab.imshow(pix, cmap=pylab.cm.bone)
pylab.show() # cmap

'''

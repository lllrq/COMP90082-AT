import pydicom

"""
extract all gantry angle from file_path  
if you want use this function, 
please upload one file_path which is a dicom file
"""
def extractGantryAngle(file_path):
    file_path = "C:/Users/zhouz/Documents/SP/YellowLvlIII_7a.dcm"
    ds = pydicom.dcmread(file_path,force=True)
    list1 = []
    for bs in ds.BeamSequence:
        for cp in bs.ControlPointSequence:
            if hasattr(cp,'GantryAngle'):
                list1.append(cp.GantryAngle)
                #print(cp.GantryAngle)
    return list1;
    # print(ds.BeamSequence[0].ControlPointSequence[0].GantryAngle)

def TestGantryAngle(file_path):
    ds = pydicom.dcmread(file_path, force=True)
    list1 = [150.0,60.0]


file_path = "/Users/seven/Desktop/YellowLvlIII_7a.dcm"
extractGantryAngle(file_path)





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
# COMP90082-AT


how to use it?
so easy, two steps:

1: put dicom file path to DICOM_File_Path file;
2: run the GantryAngle file;
3: check the csv file in directory which is same with DICOM_File_Path file;

AT-wombat is a pure python package for extracting params from DICOM files. 
It was made for extracting and validating DICOM data in an easy "pythonic" way.  


Until current,
I define one extractGantryAngle(file_path) function which is used to extract all Gantry Angle.

also, this file depend on pydicom package,
if you want invoke this function, 
please pip install pydicom first.  
 
 
 prepare:
 
 1. use "pip install openpyxl" in terminal in order to use python to deal with excel.
 
  
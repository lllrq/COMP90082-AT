# COMP90082-AT


## 1. introduction:
AT-wombat is a pure python package for extracting params from DICOM files and validating with given truth table.  


## 2. steps of using
how to use this system to validate DICOM file?
only three steps:
1. put dicom file directory path to DICOM_File_Path file in 'Path' directory;
2. modify truth table value in 'Path' directory if you want;
3. run auto_validate.py file to run this file.


## 3. prepare & dependency:
this python file depend on some package,
if you want to invoke this function, please use pip install to install following packages.
1. pydicom: pip install pydicom, which is used to deal with DICOM file;
2. csv: pip install csv, which is used to deal with csv file;
3. openpyxl: pip install openpyxl, which is used to deal with excel file; 


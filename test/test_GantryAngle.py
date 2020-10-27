#!/usr/bin/python3

'''
This script runs a set of unittests on the Python
code named auto_validate.py written for the subject
Software Project (COMP90082)

Execute by entering your Anaconda environment and
typing from the command line:

python test_GA.py -v

This will test a few functions and their outputs
for their correctness.
'''

import unittest
import os
import auto_validate
from parameters import collimator, gantry_angle, SSD, wedge, prescription_dose


class TestFunctions(unittest.TestCase):

    def setUp(self):
        ''' Sets up a few variables to run test cases in Task 1'''
        self.filepath = "C:/Users/zhouz/Documents/SP/DICOM/YellowLvlIII_1a.dcm"
        self.res_gantry_angle = 0.0
        self.res_SSD = 1000
        self.res_wedge = 0
        self.res_collimator = 0
        self.res_prescription_dose = 2.0

    def test_import(self):
        ''' Test the import_csv function '''
        ga_output = gantry_angle.extract_gantry_angle(self.filepath)
        self.assertTrue(isinstance(ga_output, list),
                        "Output not a list. \
                        Ignore this error if you defined a class.")

    def test_gantry_angle(self):
        ''' Tests the function '''
        # self.ga_output = [int(x) for x in self.ga_output]

        ga_output_list = gantry_angle.extract_gantry_angle(self.filepath)
        self.assertTrue(isinstance(ga_output_list, list),
                        "Output not a list.")
        self.assertTrue(isinstance(ga_output_list[0], float),
                        "Output not a float, seems unlikely")
        self.assertEqual(ga_output_list[0], self.res_gantry_angle,
                         "Function does not return exactly 0.0")

    def test_SSD(self):
        ssd_output_list = SSD.extract_SSD(self.filepath)
        self.assertTrue(isinstance(ssd_output_list, list),
                        "Output not a list.")
        self.assertTrue(isinstance(ssd_output_list[0], float),
                        "Output not a float, seems unlikely")
        self.assertEqual(ssd_output_list[0], self.res_SSD,
                         "Function does not return exactly 1000.0")


    def test_wedge(self):
        wedge_output_list = wedge.extract_wedge(self.filepath)
        self.assertTrue(isinstance(wedge_output_list, list),
                        "Output not a list.")
        self.assertTrue(isinstance(wedge_output_list[0], int),
                        "Output not a int, seems unlikely")
        self.assertEqual(wedge_output_list[0], self.res_wedge,
                         "Function does not return exactly 0.0")

    def test_collimator(self):
        collimator_output_list = collimator.extract_collimator(self.filepath)
        self.assertTrue(isinstance(collimator_output_list, list),
                        "Output not a list.")
        self.assertTrue(isinstance(collimator_output_list[0], float),
                        "Output not a float, seems unlikely")
        self.assertEqual(collimator_output_list[0], self.res_collimator,
                         "Function does not return exactly 0.0")

    def test_prescription_dose(self):
        prescription_dose_output_list = prescription_dose.extract_prescription_dose(self.filepath)
        self.assertTrue(isinstance(prescription_dose_output_list, list),
                        "Output not a list.")
        self.assertTrue(isinstance(prescription_dose_output_list[0], float),
                        "Output not a float, seems unlikely")
        self.assertEqual(prescription_dose_output_list[0], self.res_prescription_dose,
                         "Function does not return exactly 2.0")

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3

''' This script runs a set of unittests on the Python
    code named GantryAngle.py written for the subject
    Software Project (COMP90082)

    Execute by entering your Anaconda environment and
    typing from the command line:

    python test_GA.py -v

    This will test a few functions and their outputs
    for their correctness. '''

import unittest
import os
import GantryAngle


class TestTaskOne(unittest.TestCase):
    def setUp(self):
        ''' Sets up a few variables to run test cases in Task 1'''
        self.filepath = "C:/Users/zhouz/Documents/SP/YellowLvlIII_7a.dcm"
        self.test_answer = 150.0


    def test_import(self):
        ''' Test the import_csv function '''
        ga_output = GantryAngle.extractGantryAngle(self.filepath)
        self.assertTrue(isinstance(ga_output, list),
                        "Output not a list. \
                        Ignore this error if you defined a class.")

    def test_project_output(self):
        ''' Tests the function '''
        ga_output_list = GantryAngle.extractGantryAngle(self.filepath)
        self.assertTrue(isinstance(ga_output_list , list),
                        "Output not a list.")
        self.assertTrue(isinstance(ga_output_list[0], float),
                        "Output not a float, seems unlikely")
        self.assertEqual(ga_output_list[0], self.test_answer,
                         "Function does not return exactly 150.0")



if __name__ == '__main__':
    unittest.main()
